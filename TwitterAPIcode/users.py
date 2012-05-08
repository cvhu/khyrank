#!/usr/bin/python


import sys
import urllib2
import json
import cPickle
import simplejson as json
import twitter
import urllib2


# key and secret granted by service provider: ask Ann if they don't work, or make your own.
CONSUMER_KEY = "gq9fdcftaxWrzKbfoAV8w"
CONSUMER_SECRET = "FbbE7YeyWqmLakHGJN2mI3ektcQcnrw7NNDzwnQmVs"
ACCESS_TOKEN = "14941231-OWaxY4zTIGUEBNfoTM1LauTxARDThUxA9f44SgYTX"
ACCESS_TOKEN_SECRET = "47qaok2YCghfQWwUZFYMc1UjlddUuTFtX7IDhdeLSQ" 



# take a m-by-n matrix and create a filename.csv
def makeCSV(filename, matrix):
    f = open(filename+'.csv', 'w+')
    for row in matrix:
        line = ""
        for element in row:
            line = line+str(element) + ','
        f.write(line[:-1]+"\n") # remove the last comma and add a newline

class User:
    #static variables	
    twapi = twitter.Api(consumer_key=CONSUMER_KEY,
                        consumer_secret=CONSUMER_SECRET,
                        access_token_key=ACCESS_TOKEN,
                        access_token_secret=ACCESS_TOKEN_SECRET)


    def __init__(self, uid=None, screenName=None, test=False):
        if not test:
            if uid:
                self.userObj = User.twapi.GetUser(uid)
            elif screenName:
                self.userObj = User.twapi.GetUser(screenName)
                
            self.uid = self.userObj.id
            self.screenName = self.userObj.screen_name
            # will become a list of all follower uids (strings)
            self.followers = self.lookupFollowers()    

        else:  # TESTING
            self.uid = uid
            self.screenName = screenName	
            self.followers = []


    def __str__(self):
        return self.userObj.screen_name


    # make a set of fake followers for testing
    # just hand it a list of fake uid strings
    def makeFollowers(self, fake_uid_list):
        self.followers = fake_uid_list
        

    #use API to get followers as an array follower ids
    def lookupFollowers(self):
        host = "https://api.twitter.com/1/followers/ids.json?cursor=-1&"
        print self
        if self.screenName!=None:
            url = host+"screen_name="+str(self.screenName)
        else:
            url = host+"user_id="+str(self.uid)
        print url
        try:
            req = urllib2.Request(url)
            response_stream = urllib2.urlopen(req)
            response = response_stream.read()
            response_stream.close()
            data = json.loads(response)
            return data['ids']
        except:
            return []
        
    # accessor for followers
    def getFollowers(self):
        return self.followers


    # number of followers
    def getFollowerCount(self):
        return size(self.followers)


    def printFollowers(self):
        for f in self.followers:
            print f

			

class TwitterGraph:
    def __init__(self):
        # a dictionary of users, keyed on uid, with User objects as values 
        self.users = {}


    def lookupAllFollowers(self):
        for user in self.users.values():
            user.lookupFollowers()
            print 'uid: ', user.uid, ' sn: ', user.screenName
            user.printFollowers()


    def addUser(self, uid=None, screenName=None):
        newuser = User(uid, screenName)
        self.users[newuser.uid] = newuser 


    def printUsers(self):
        for item in self.users.keys():
            user = self.users[item]
            print user, item, " has: ",len(user.getFollowers()), " followers:", user.getFollowers()
        

    # number of nodes in the graph
    def size(self):
        return len(self.users)


    def getFollowersDict(self):
        followers = {}
        for uid in self.users.keys():
            followers[uid] = self.users[uid].getFollowers()
        return followers
    
    def getA(self):
        followers = self.getFollowersDict()
        candidates = followers.keys()
        A = []
        A.append(candidates)
        for candidate in candidates:
            row = [0]*len(candidates)
            for follower in followers[candidate]:
                if follower in candidates:
                    ind = candidates.index(follower)
                    row[ind] = 1
            A.append(row)
        return A



if __name__ == "__main__":
    target_username = "aiclass"
    target = User(screenName=target_username)
    follower_ids = target.getFollowers()
    print str(len(follower_ids)) + ' followers to go'
    G = TwitterGraph()
    for follower_id in follower_ids:
        G.addUser(uid=follower_id)
    A = G.getA() # why does it always return the same set of followers?
    makeCSV(target_username, A)
    # G.lookupAllFollowers()
    #G.printUsers()


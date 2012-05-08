#  gets more complex data, 
# creates a sparse array (implemented as a dictionary of dictionaries) representing
# how many times user in row i has @ mentioned user in col j in all tweets
# note, use mentionsArrayFormat.py to read the output pickle from this code and write 
# to a CSV for MATLAB.  File will be large... O_o
import re, cPickle
import urllib2
import simplejson as json

# infochimps stuff
API_KEY = 'akilzer-UIqIhWBpM0zto8Uw9QW0uaM7569'
CMDSTR = r'http://api.infochimps.com/social/network/tw/util/map_id?apikey=%s&screen_name=%s'
json_d = json.JSONDecoder()


# parsing stuff
pattern = re.compile(r'(\d+)\s(\d+)\s(.*)(20\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d)\s*')
retweetPattern = re.compile(r'RT\s@(\w+)(.*)')
mentionPattern = re.compile('@(\w+).*')


# open the uid mapping
mf = open('mapping.pickle', 'rb')
mapping = cPickle.load(mf)
mf.close()


#f = open('training_tweets_time.txt', 'r+')
f = open('test_tweets_time.txt', 'r+')


mentionArray = {}

for line in f.readlines():
    try:
        (user, b, tweet, time) = pattern.match(line).groups()

        flag = False        
        # process user
        retweet = retweetPattern.match(tweet)

        if retweet is not None:
            (RTuser, rest) = retweet.groups()
        else:
            rest = tweet

    except ValueError:
        pass
    except AttributeError:
        pass

    try:

        mentions = mentionPattern.findall(rest)

        if user not in mentionArray:
            mentionArray[user] = {}

        for m in mentions:
            if m in mapping:
                uid = mapping[m]
                print 'found user', m
            else:
                #do the lookup
                try:
                    url = CMDSTR % (API_KEY, m)
                    response = urllib2.urlopen(url)
                    data = json_d.decode(response.read())
                    uid = data['user_id']
                    mapping[m] = uid
                    print 'adding user', m
                except Exception, e:
                    # if we still can't get the user, just punt
                    print 'missing', m 
                    continue

            if uid in mentionArray[user]:
                mentionArray[user][uid] += 1
            else:
                mentionArray[user][uid] = 1


    except ValueError:
        pass

    except AttributeError:
        pass

f.close()
# write out data using sorted list to maintain structure


# store it in a pickle
mf = ('mapping.pickle', 'wb')
cPickle.dump(mapping, mf)


df = ('mentionsDict.pickle', 'wb')
cPickle.dump(mentionArray, df)

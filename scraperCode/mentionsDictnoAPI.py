#  gets more complex data, 
# creates a sparse array (implemented as a dictionary of dictionaries) representing
# how many times user in row i has @ mentioned user in col j in all tweets
# note, use mentionsArrayFormat.py to read the output pickle from this code and write 
# to a CSV for MATLAB.  File will be large... O_o
import re, cPickle


#users = set()
#userf = open('sorted_users.txt', 'r+')

#for line in userf:
#    users.add(line.strip())

#names = open('numeric2screen', 'r+')

#nMapping = {}

#count = 0
#for line in names:
#    try:
#        (id, name) = line.split()
#        if id in users:
#            print 'found'
#            nMapping[name] = id
#    except ValueError:
#        print 'error on', line
#    count += 1
#    if (count % 1000 == 0):
#        print count

#names.close()

#outf = open('numeric2screenMatches.pickle', 'wb')
#cPickle.dump(nMapping, outf)
#outf.close()

#print 'Pickling done'

# parsing stuff
pattern = re.compile(r'(\d+)\s(\d+)\s(.*)(20\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d)\s*')
retweetPattern = re.compile(r'RT\s@(\w+)(.*)')
mentionPattern = re.compile('@(\w+).*')


# open the uid mapping
mf = open('numeric2screenMatches.pickle', 'rb')
mapping = cPickle.load(mf)
mf.close()


f = open('training_tweets_time.txt', 'r+')
#f = open('test_tweets_time.txt', 'r+')

missing = set()
mentionArray = {}

count = 0

for line in f:
    count += 1
    if (count % 1000 == 0):
        print count
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
            elif m in missing:
                print 'given up', m
                continue                
            #elif m in Nmapping:
            #    uid = mapping[m]
            #    print 'found user', m
            else:
                print 'missing', m
                missing.add(m)
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
#mf = ('map.pickle', 'wb')
#cPickle.dump(mapping, mf)


df = open('mentionsDict.pickle', 'wb')
cPickle.dump(mentionArray, df)

#  gets more complex data, 
# creates a sparse array (implemented as a dictionary of dictionaries) representing
# how many times user in row i has retweeted user in col j in all tweets
# note, use retweetArrayFormat.py to read the output pickle from this code and write 
# to a CSV for MATLAB.  File will be large... O_o
import re, cPickle


# parsing stuff
pattern = re.compile(r'(\d+)\s(\d+)\s(.*)(20\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d)\s*')
retweetPattern = re.compile(r'RT\s@(\w+)(.*)')


# open the uid mapping
mf = open('numeric2screenMatches.pickle', 'rb')
mapping = cPickle.load(mf)
mf.close()


f = open('training_tweets_time.txt', 'r+')
#f = open('test_tweets_time.txt', 'r+')

missing = set()
retweetArray = {}


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

        if user not in retweetArray:
            retweetArray[user] = {}

        if retweet is not None:
            (RTuser, rest) = retweet.groups()

            if RTuser in mapping:
                uid = mapping[RTuser]
                print 'found user', RTuser
            elif RTuser in missing:
                print 'given up', RTuser
                continue                
            else:
                print 'missing', RTuser
                missing.add(RTuser)
                continue

            if uid in retweetArray[user]:
                retweetArray[user][uid] += 1
            else:
                retweetArray[user][uid] = 1


    except ValueError:
        pass
    except AttributeError:
        pass

f.close()
# write out data using sorted list to maintain structure


# store it in a pickle
#mf = ('map.pickle', 'wb')
#cPickle.dump(mapping, mf)


df = open('retweetDict.pickle', 'wb')
cPickle.dump(retweetArray, df)

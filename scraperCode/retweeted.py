#  gets more complex data, like retweet sources
import re


pattern = re.compile(r'(\d+)\s(\d+)\s(.*)(20\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d)\s*')
retweetPattern = re.compile(r'RT\s@(\w+).*')

#f1 = open('tweet_retweet_counts.txt', 'r+')

#userStats = {}

#for line in f1.readlines():
#        userStats[line.split()[1]] = 0
#f1.close()        



f = open('training_tweets_time.txt', 'r+')
#f = open('test_tweets_time.txt', 'r+')



userStats = {}


for line in f.readlines():
    try:
        
        (a, b, tweet, time) = pattern.match(line).groups()

        flag = False        
        # process user
        retweet = retweetPattern.match(tweet)

        if retweet is not None:
            RTuser = retweet.groups()[0]
            if RTuser in userStats:
                userStats[RTuser] += 1        
            else:
                userStats[RTuser] = 1

    except AttributeError:
        last = line
        flag = True


# write out data        

for user, data in userStats.items():
    
    print user, data

# be sure to use bash sort to maintain order
# need to get mapping of names to ids

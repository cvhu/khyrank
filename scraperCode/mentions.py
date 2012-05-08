#  gets more complex data, like retweet sources
import re


pattern = re.compile(r'(\d+)\s(\d+)\s(.*)(20\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d)\s*')
retweetPattern = re.compile(r'RT\s@(\w+)(.*)')
mentionPattern = re.compile('@(\w+).*')


uf = open('sorted_users.txt', 'r+')

#f = open('training_tweets_time.txt', 'r+')
f = open('test_tweets_time.txt', 'r+')



userStats = {}


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

        if user in userStats:
            userStats[user] += len(mentions)
        else:
            userStats[user] = len(mentions)

    except ValueError:
        pass

    except AttributeError:
        pass


# write out data using sorted list to maintain structure

for line in uf.readlines():
    user = line.split()[0]
    if user in userStats:
        data = userStats[user]
        print user, data
    else:
        print user, 0




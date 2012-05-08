
import re


pattern = re.compile(r'(\d+)\s(\d+)\s(.*)(20\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d)\s*')


uf = open('sorted_users.txt', 'r+')

f = open('training_tweets_time.txt', 'r+')
#f = open('test_tweets_time.txt', 'r+')

flag = False
last = ''
count = 0
userStats = {}


for line in f.readlines():
    try:
        if flag:
            current = last + line
            last = ''
        else:
            current = line
        
        (a, b, tweet, time) = pattern.match(current).groups()

        flag = False        
        # process user
        if a in userStats:
            userStats[a][0] += 1  # count the tweet
        else:
            userStats[a] = [1, 0]

        if tweet.startswith('RT @'):
            userStats[a][1] += 1

    except AttributeError:
        last = line
        flag = True
        

for line in uf.readlines():
    user = line.split()[0]
    if user in userStats:
        data = userStats[user]
        (tweets, retweets) = data
        print user, tweets, retweets
    else:
        print user, 0, 0

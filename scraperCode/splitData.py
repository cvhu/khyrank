
import re


pattern = re.compile(r'(\d+)\s(\d+)\s(.*)(20\d\d-\d\d-\d\d\s\d\d:\d\d:\d\d)\s*')


f1 = open('originalData/training_set_tweets.txt', 'r+')
f2 = open('originalData/test_set_tweets.txt', 'r+')

flag = False
last = ''
count = 0
test_data = []
training_data = []
files = [f1, f2]

for f in files:

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


            if time.startswith('2009-09') or time.startswith('2009-10') or time.startswith('2009-11'):
                training_data.append(current)
            else:
                test_data.append(current)




        except AttributeError:
            last = line
            flag = True
        

trainFile = open('training_tweets_time.txt', 'w+')
testFile = open('test_tweets_time.txt', 'w+')

# write the data

trainFile.write(''.join(training_data))
testFile.write(''.join(test_data))

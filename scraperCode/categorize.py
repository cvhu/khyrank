
trainf = open('training_mentionedUID_sorted.txt', 'r+')
testf = open('test_mentionedUID_sorted.txt', 'r+')

#trainf = open('training_retweeted_countsUID_sorted.txt', 'r+')
#testf = open('test_retweeted_countsUID_sorted.txt', 'r+')

training = set()
test = set()


n = 31544

thresh = 0

count = 0
for line in trainf:
    if count > n:
        break
    (num, uid) = line.split()
    if num > thresh:
        training.add(uid)
        count += 1

trainCount = count

count = 0
for line in testf:
    if count > n:
        break
    (num, uid) = line.split()
    if num > thresh:
        test.add(uid)
        count += 1

intersect = test.intersection(training)

i = 0

for uid in test:
    if uid in training:
        i += 1


print thresh
print len(intersect), i,  'out of', n

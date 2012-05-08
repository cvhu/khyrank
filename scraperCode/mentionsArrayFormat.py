import cPickle

f = open('mentionsDict.pickle', 'rb')
mentionArray = cPickle.load(f)
f.close()

uf = open('sorted_users.txt', 'r+')

userList = []
for line in uf:
    user = line.split()[0]
    userList.append(user)

uf.close()

col = len(userList)

outf = open('mentionsArray.txt', 'w+')

empty = col * '0 '

for userRow in userList:
    if userRow in mentionArray:
        outf.write('%s ' % userRow)
        for userCol in userList:
            if userCol in mentionArray[userRow]:
                outf.write('%s ' % mentionArray[userRow][userCol])
            else: 
                outf.write('0 ')
        outf.write('\n')

    else:
        outf.write('%s %s\n' % (user, empty))



# remove duplicates from the list of all users


f = open('sorted_users.txt', 'r+')

users = set()

for line in f.readlines():
    #(uid, location) = line.split('\t')
    uid = line.strip('\n')
    users.add(uid)


f.close()

f = open('sorted_users2.txt', 'w+')

f.write('\n'.join(users))

f.write('\n') # add one last newline so word counts will be the same

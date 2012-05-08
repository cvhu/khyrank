
size = ('15K', 15000)

L2f = open('L2result_%s.txt' % size[0], 'r+')
dcf = open('dc%d_sorted.txt' % size[1], 'r+')
prf = open('pr%dsorted.txt' % size[1], 'r+')

N = 150

L2 = set()
dc = set()
pr = set()

count = 0
for line in L2f:
    if count > N:
        break
    count += 1
    uid = line.strip()
    L2.add(uid)

count = 0
for line in dcf:
    if count > N:
        break
    count += 1
    uid = line.strip()
    dc.add(uid)

count = 0
for line in prf:
    if count > N:
        break
    count += 1
    uid = line.strip()
    pr.add(uid)


pr_int_dc = pr.intersection(dc)
pr_int_l2 = pr.intersection(L2)
l2_int_dc = L2.intersection(dc)
center = len(pr_int_dc.intersection(L2))

print 'Page Rank and Degree Count'

print len(pr_int_dc) - center


print 'Page Rank and L2'

print len(pr_int_l2) - center

print 'L2 and Degree Count'

print len(l2_int_dc) - center


print 'Center'

print center

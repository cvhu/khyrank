#!/usr/bin/python

def makeQAMat(usersFileName, graphFileName, outFileName):
	u = open(usersFileName, 'r')
	g = open(graphFileName, 'r')
	o = open(outFileName, 'w+')
	
	u2 = open(usersFileName, 'r')
	u2line = u2.readline()
	oline = ''
	while u2line:
		user = u2line.split()[0]
		oline = oline + user + ','
		u2line = u2.readline()
	u2.close()
	o.write(oline[:-1]+"\n")		

	uline = u.readline()
	interval = 1000000
	user = uline.split()[0]
	row = ''
	u2 = open(usersFileName, 'r')

	u2line = u2.readline()
	user2 = u2line.split()[0]

	lc = 0
	gline = g.readline()
	while gline:
		# print user, ':', user2, '----', gline
		if lc%interval == 0:
			print str(lc/interval) + 'M--------------------------'
		glist = gline.split()
		if glist[0] == user:
			if glist[1] == user2:
				row = row + '1,'
				gline = g.readline()
				lc = lc + 1
				u2line = u2.readline()
				user2 = u2line.split()[0]
			elif int(glist[1]) < int(user2):
				gline = g.readline()
				lc = lc + 1			
			elif int(glist[1]) > int(user2):
				row = row + '0,'
				u2line = u2.readline()
				if u2line:
					user2 = u2line.split()[0]
				else:
					o.write(row[:-1]+"\n")
					row = ''
					uline = u.readline()
					user = uline.split()[0]
					u2.close()
					u2 = open(usersFileName, 'r')
					u2line = u2.readline()
					user2 = u2line.split()[0]										
		elif int(glist[0]) < int(user):
			gline = g.readline()
			lc = lc + 1			
		elif int(glist[0])> int(user):
			# u2line = u2.readline()
			while u2line:
				row = row + '0,'
				u2line = u2.readline()
			o.write(row[:-1]+"\n")
			row = ''
			uline = u.readline()
			user = uline.split()[0]
			u2.close()
			u2 = open(usersFileName, 'r')
			u2line = u2.readline()
			user2 = u2line.split()[0]
	while uline:
		while u2line:
			row = row + '0,'
			u2line = u2.readline()		
		o.write(row[:-1]+"\n")
		row = ''
		uline = u.readline()
		if uline:
			user = uline.split()[0]
		else:
			pass
		u2.close()
		u2 = open(usersFileName, 'r')
		u2line = u2.readline()
		user2 = u2line.split()[0]		

if __name__ == '__main__':
	# usersFileName = 'sorted_users_by_int.test.txt'
	usersFileName = '/scratch/cluster/akilzer/twitterCIKM/sorted_users.txt'
	# graphFileName = 'twitter_rv.test.net'
	graphFileName = '/scratch/cluster/akilzer/twitterGraph/twitter_rv.net'
	outFileName = 'sorted_users_new.amat.csv'
	makeQAMat(usersFileName, graphFileName, outFileName)

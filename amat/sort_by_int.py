#!/usr/bin/python

if __name__ == "__main__":
	f = open('sorted_users.txt', 'r')
	out = open('sorted_users_by_int.txt', 'w+')
	a = []
	line = f.readline()
	c = 0
	while line:
		c = c+1
		if c%1000 == 0:
			print c
		a.append(int(line.split()[0]))
		line = f.readline()
	a.sort()
	for i in a:
		out.write(str(i)+'\n')
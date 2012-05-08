#!/usr/bin/python

# .dict2csv

import sys


# take a m-by-n matrix and create a filename.csv
def makeCSV(filename, matrix):
	f = open(filename+'.csv', 'w+')
	for row in matrix:
		line = ""
		for element in row:
			line = line+str(element) + ','
		f.write(line[:-1]+"\n") # remove the last comma and add a newline
		
	
# test code for getting followers dictionary
def getDict():
	followers = {}
	# for i in range(10):
	# 	followers[i] = [(j+1)%10 for j in range(i)]
	followers['a'] = ['b', 'z', 'x']
	followers['b'] = ['x', 'c', 'd']
	followers['c'] = ['a']
	followers['d'] = ['z', 'b']
	followers['x'] = ['c', 'd', 'b', 'a']
	followers['z'] = ['alpha', 'a', 'd', 'x']
	return followers
		
# it takes a dictionary of followers and generate an adjacency matrix
# each row indicates the corresponding followers within the given set (all keys)
# i.e. for A_ij = 1, column j is following row i. A_ij = 0 if otherwise
def adjMat(followers):
	candidates = followers.keys()
	A = []
	A.append(candidates)
	for candidate in candidates:
		row = [0]*len(candidates)
		for follower in followers[candidate]:
			if follower in candidates:
				ind = candidates.index(follower)
				row[ind] = 1
		A.append(row)
	return A

def getMat():
	return [range(10) for i in range(10)]



if __name__ == '__main__':
	# mat = getMat()
	followers = getDict()
	A = adjMat(followers)
	makeCSV('test', A)
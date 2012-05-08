#!/usr/bin/python


import sys


def makeCSV(filename, matrix):
    f = open(filename+'.csv', 'w+')
    for row in matrix:
        line = ""
        for element in row:
            line = line+str(element) + ','
        f.write(line[:-1]+"\n") # remove the last comma and add a newline


def parseCandidates(filename):
	f = open(filename, 'r')
	line = f.readline()
	candidates = []
	while line:
		line_list = line.split()
		candidates.append(line_list[0])
		line = f.readline()
	return candidates
	
def makeAMat(candidates, netfile):
	f = open(netfile, 'r')
	A = []
	A.append(candidates)
	for i in range(len(candidates)):
		row = [0]*len(candidates)
		A.append(row)
	line = f.readline()
	c = 0
	while line:		
		c = c + 1
		if c%1000000 == 0:
			print str(c/1000000)+'M ------------------------------------------------'	
		if c%1000000000 == 0:
			print str(c/1000000000)+'B *********************************************'	
			# makeCSV('twitter_rv_w_test_set_users_'+str(c/1000000)+'M', A)
		line_list = line.split()
		if line_list[0] in candidates:
			i = candidates.index(line_list[0])
			if line_list[1] in candidates:
				print line_list,
				j = candidates.index(line_list[1])
				A[i][j] = 1
		line = f.readline()
	return A


if __name__ == '__main__':
	candidates = parseCandidates('/scratch/cluster/akilzer/twitterCIKM/sorted_users.txt')
	A = makeAMat(candidates, '/scratch/cluster/akilzer/twitterGraph/twitter_rv.net')
	makeCSV('twitter_rv_w_sorted_users', A)
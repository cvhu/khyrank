#!/usr/bin/python

import re

def parseCandidates(filename):
	f = open(filename, 'r')
	line = f.readline()
	candidates = []
	while line:
		line_list = line.split()
		candidates.append(line_list[0])
		line = f.readline()
	return candidates

def makeCSV(filename, matrix):
    f = open(filename+'.csv', 'w+')
    for row in matrix:
        line = ""
        for element in row:
            line = line+str(element) + ','
        f.write(line[:-1]+"\n") # remove the last comma and add a newline

def makeAMatFromRaw(candidates, rawFile):
	f = open(rawFile, 'r')
	A = []	
	
	A.append(candidates)
	for i in range(len(candidates)):
		row = [0]*len(candidates)
		A.append(row)
	line = f.readline()
	while line:		
		brackets = re.findall("\[[^\[^\].]+\]", line)
		for bracket in brackets:			
			followings = re.findall("\d+",bracket)
			i = candidates.index(followings[0])
			j = candidates.index(followings[1])
			A[i][j] = 1
			print i,j
		line = f.readline()
	return A


if __name__ == '__main__':
	rawFile = "amat.raw"
	candidates = parseCandidates('test_set_users.txt')
	A = makeAMatFromRaw(candidates, rawFile)
	makeCSV('full1468M', A)
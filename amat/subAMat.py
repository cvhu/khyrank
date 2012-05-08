#!/usr/bin/python


if __name__ == '__main__':
	N = 10
	amatFile = "sorted_users_new.amat.csv"
	outFile = amatFile.split('.')[0] + '_sub' + str(N) + '.csv'
	af = open(amatFile, 'r')
	of = open(outFile, 'w+')
	for i in range(N+1):
		of.write(','.join(af.readline().split(',')[:N]) + '\n')
	af.close()
	of.close()
	

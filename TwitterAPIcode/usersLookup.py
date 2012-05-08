#!/usr/bin/python

# .interactionsFor "screenName1" "screenName2"

import sys
import urllib2
import json

def fetchJSON(user_id):
	uri = "https://api.twitter.com/1/users/show.json?id="+user_id
	# print "HTTP GET.... ", uri
	# try:
	req = urllib2.Request(uri)
	response_stream = urllib2.urlopen(req)
	response = response_stream.read()
	response_stream.close()
	data = json.loads(response)
	return data
	# except:
	# 	return 0

if __name__ == '__main__':
	usersFile = 'khy15.txt'
	outFile = usersFile.split('.')[0] + '.html'
	uf = open(usersFile, 'r')
	of = open(outFile, 'w+')
	uline = uf.readline()
	while uline:
		ulist = uline.split()
		# print ulist
		if len(ulist) != 3:
			print uline
		else:
			userJSON = fetchJSON(ulist[0])
			try:				
				print userJSON['name'],'&', ulist[1],'&', ulist[2],'\\\\'
			except:
				print ulist[0],'&', ulist[1],'&', ulist[2],'\\\\'
		uline = uf.readline()
#!/usr/bin/python

# .interactionsFor "screenName1" "screenName2"

import sys
import urllib2
import json

class User:
	
	def __init__(self, uid=None, screenName = None):
		self.uid = uid
		self.screenName = screenName
		self.followers = FetchJSON.getFollowers(self)

	def getFollowers(self):
		return self.followers



class FetchJSON:
	
	def getFollowers(User):
		


def main():
	host = "https://api.twitter.com/1/followers/ids.json?cursor=-1&screen_name="
	url = host+id1
	print "HTTP GET.... ", url
	req = urllib2.Request(url)
	response_stream = urllib2.urlopen(req)
	response = response_stream.read()
	response_stream.close()
	data = json.loads(response)
	print len(data['ids'])

if __name__ == '__main__':
	main()
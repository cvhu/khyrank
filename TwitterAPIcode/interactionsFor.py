#!/usr/bin/python

# .interactionsFor "screenName1" "screenName2"

import sys
import urllib2
import json

def main():
	id1 = sys.argv[1]
	id2 = sys.argv[2]
	print id1, id2
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
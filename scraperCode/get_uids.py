#  gets more complex data, like retweet sources
import urllib2, cPickle
import simplejson as json
import time


#infochimps
API_KEY = 'akilzer-UIqIhWBpM0zto8Uw9QW0uaM7569'

CMDSTR = r'http://api.infochimps.com/social/network/tw/util/map_id?apikey=%s&screen_name=%s'

json_d = json.JSONDecoder()

f1 = open('test_retweeted_counts.txt')
f2 = open('training_retweeted_counts.txt')


mf = open('mapping.pickle', 'rb')

mapping = cPickle.load(mf)

mf.close()
#pf = open('missing_users.pickle', 'rb')

missing_users = set()

#pf.close()

for f in [f1, f2]:

    for line in f.readlines():
        try:
            (user, count) = line.split()
            
            if user in mapping:
                print user, " matched previously"
            else:

                url = CMDSTR % (API_KEY, user)
                response = urllib2.urlopen(url)
                data = json_d.decode(response.read())
                mapping[user] = data['user_id']
                print user, data['user_id']

        except urllib2.HTTPError:
            missing_users.add(user)
        except ValueError:
            # first line does not have a name... why?
            pass
        except Exception, e:
            missing_users.add(user)
    



outf = open('mapping.pickle', 'wb')
cPickle.dump(mapping, outf)

outf2 = open('missing_users.pickle', 'wb')
cPickle.dump(missing_users, outf2)

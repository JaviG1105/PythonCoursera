import json, urllib

serviceURL = 'http://www.omdbapi.com/?'

title = raw_input('Type the name of the movie: ')
if len(title) < 1 :
    print 'Error in title'

url = serviceURL + urllib.urlencode({'t':title, 'plot':'short', 'r':'json'})
print 'Retrieving: ', url, '...'
uh = urllib.urlopen(url)
data = uh.read()
print 'Retrieved: ', len(data), 'characters'
js = json.loads(str(data))

runtime = js["Runtime"]
runtime = runtime[:3]
timeHrs = int(runtime) / 60

print title.upper(),': Runtime in minutes:', runtime, ', in HOURS:' ,timeHrs
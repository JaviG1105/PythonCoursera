import urllib, json

serviceUrl = 'http://python-data.dr-chuck.net/geojson?'
address = 'University of Piraeus Athens'

url = serviceUrl + urllib.urlencode({'sensor':'false', 'address':address})

uh = urllib.urlopen(url)
data = uh.read()

js = json.loads(str(data))

print 'URL retrieved: ', url
print 'Length of the data: ', len(data)
print 'Place ID requested: ', js["results"][0]["place_id"]


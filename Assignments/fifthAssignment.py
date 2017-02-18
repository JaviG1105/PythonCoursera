import urllib, json

url = "http://python-data.dr-chuck.net/comments_353500.json"

uh = urllib.urlopen(url)
data = uh.read()
sum = 0
js = json.loads(str(data))

for x in js["comments"] :
    sum += x["count"]

print 'Sum of all count values: ', sum
import xml.etree.ElementTree as ET
import urllib.request

xmlURL = 'http://python-data.dr-chuck.net/comments_353496.xml'

uh = urllib.request.urlopen(xmlURL)
data = uh.read()
tree = ET.fromstring(data)

list = tree.findall('.//count')
sum = 0
for item in list:
    sum += int(item.text)

print (sum)

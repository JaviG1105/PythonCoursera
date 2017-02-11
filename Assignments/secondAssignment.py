from BeautifulSoup import *
import urllib

sum = 0
url = 'http://python-data.dr-chuck.net/comments_353499.html'

html = urllib.urlopen(url).read()
soup = BeautifulSoup(html)

tags = soup('span')


for tag in tags:
    sum += int(tag.contents[0])

print 'Result:',sum

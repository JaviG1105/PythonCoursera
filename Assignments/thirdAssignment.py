from BeautifulSoup import *
import urllib

url = 'http://python-data.dr-chuck.net/known_by_Shaiza.html'

for i in range(7):
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html)

    tags = soup('a')
    url = tags[17].get('href', None)
    print tags[17].get('href', None)
    
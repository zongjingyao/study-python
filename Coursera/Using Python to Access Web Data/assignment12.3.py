import urllib
from BeautifulSoup import *

url = raw_input("Enter URL: ")
count = int(raw_input("Enter count: "))
position = int(raw_input("Enter position: ")) - 1

for i in range(count):
    html = urllib.urlopen(url).read()

    soup = BeautifulSoup(html)

    tags = soup('a')
    url = tags[position].get('href', None)
    last_name = tags[position].contents[0]
    
print last_name
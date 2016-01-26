import json
import urllib

serviceurl = "http://python-data.dr-chuck.net/geojson?"
address = raw_input("Enter address: ")
url = serviceurl + urllib.urlencode({'address': address})
connectio = urllib.urlopen(url)
data = connectio.read()

info = json.loads(data)
print info["results"][0]["place_id"]
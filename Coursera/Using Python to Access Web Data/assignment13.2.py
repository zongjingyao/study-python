import json
import urllib

url = raw_input("Enter URL: ")
connection = urllib.urlopen(url)
data = connection.read()

info = json.loads(data)
sum = 0
for item in info["comments"]:
    sum += int(item["count"])
print sum
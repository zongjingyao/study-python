import urllib
import xml.etree.ElementTree as ET

url = raw_input("Enter location:")
data = urllib.urlopen(url).read()

trees = ET.fromstring(data)
counts = trees.findall(".//count")
print sum([int(count.text) for count in counts])
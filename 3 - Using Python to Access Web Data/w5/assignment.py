import urllib.request
from bs4 import BeautifulSoup
import xml.etree.ElementTree as ET

data = urllib.request.urlopen("http://py4e-data.dr-chuck.net/comments_628640.xml").read()
xml_data = ET.fromstring(data)
search_str = "comments/comment"
count_tags = xml_data.findall(search_str)

counts = 0
total_count = 0

for tag in count_tags:
  count = tag.find('count')
  counts = counts + 1
  total_count = total_count + int(count.text)

print("Count:", counts)
print("Sum:", total_count)
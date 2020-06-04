import urllib.request
import json

_url = "http://py4e-data.dr-chuck.net/comments_628641.json"
_urldata = urllib.request.urlopen(_url).read()
_data = json.loads(_urldata)

_sum = 0
for comment in _data["comments"]:
  _sum = _sum + comment["count"]

print("Sum: ", _sum)
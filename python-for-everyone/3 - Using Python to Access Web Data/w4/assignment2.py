# To run this, download the BeautifulSoup zip file
# http://www.py4e.com/code3/bs4.zip
# and unzip it in the same directory as this file

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

_url = "http://py4e-data.dr-chuck.net/known_by_Morwen.html"
_position = 18
_repetitions = 7
_name = ""

for times in range(_repetitions):
    html = urllib.request.urlopen(_url).read()
    soup = BeautifulSoup(html, "html.parser")
    tags = soup('a')
    _url = tags[_position - 1].get('href')
    _currentname = tags[_position - 1].contents[0]
    _name = _currentname
    #print(_name)

print(_name)
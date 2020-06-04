import json
import urllib
import urllib.parse
import urllib.request

#Stroring the given parameters
serviceurl = "http://py4e-data.dr-chuck.net/json?"
data_address = "South Federal University"

#Setting the GET parameters on the URL
parameters = {"sensor": "false", "address": data_address}
paramsurl = urllib.parse.urlencode(parameters)

#Generating the complete URL. Printing it in order to check if it's correct.
queryurl = serviceurl + paramsurl
print("DATA URL: ", queryurl)

#Obtaining and reading the data
data = urllib.request.urlopen(queryurl).read()

#Parsing the data and looking for the field we want.
#That field is inside the "Results" array, in its first item (if our address is 
#correct we can assume that the result would be the correct one) and on its 
#"place_id" field
jsondata = json.loads(str(data))
place_id = jsondata["results"][0]["place_id"]
print("PLACE ID: ", place_id)
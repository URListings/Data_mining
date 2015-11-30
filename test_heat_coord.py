import pycurl
import cStringIO
import sys
import json
from pprint import pprint

filename = sys.argv[1]
with open(filename, 'r') as data_file:    
    data = data_file.read()

dataArr = data.split('\n')
newString = ''
for val in dataArr:
  cood = val.split(",")
  index = len(cood)
  if cood[index-1] != "" and cood[index-2] != "":
   newString += "new google.maps.LatLng(" + cood[index-1] + "," + cood[index-2] + ")" + ",\n"
print newString 

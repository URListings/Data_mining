import sys
import json
import csv
import os

filename = sys.argv[1]
user_dict = sys.argv[2]
outfile = sys.argv[3]

if not os.path.exists(os.path.dirname(outfile)):
    os.makedirs(os.path.dirname(outfile))
with open(filename) as data_file:    
    data = json.load(data_file)
with open(user_dict) as data_file:    
    users = json.load(data_file)

def filter_location():
 locations = ""
 user_map = {}
 for proj in data:
  members = proj['members']
  if members is not None and proj['winner'] == True:
   for m in members:
    if m in users:
     user_map[m] = 1
 for key in user_map:
   loc = users[key]['location']
   if loc is not None and loc != "" and (", US" in loc or "United States" in loc):
     locations += loc
     locations += '\n'
 return locations

locations = filter_location()
locations = locations.encode("utf-8")
target = open(outfile, 'w')
target.truncate()
target.write(locations)
target.close()
print 'Done....'


import sys
import json
import csv
import os

filename = sys.argv[1]
removeFields = sys.argv[2]
outfile = sys.argv[3]
arg_type = sys.argv[4]
outfileJson = outfile + 'dict.json'
if not os.path.exists(os.path.dirname(outfile)):
    os.makedirs(os.path.dirname(outfile))
with open(filename) as data_file:    
    data = json.load(data_file)
tagdata = []
outJson = {}
removeFields = removeFields.split(",")

def filter_proj():
 for proj in data:
  tags = proj['tags'] 
  for f in removeFields:
    del proj[f]
  outJson[proj['url']] = proj
  tagdata.append(proj)

def filter_user():
 for user in data:
   user['screen_name'] = user['screen_name'].lower()
   for f in removeFields:
     del user[f]
   outJson[user['screen_name']] = user
   tagdata.append(user)

if arg_type == '1':
 filter_proj()
else:
 filter_user()

target = open(outfileJson, 'w')
target.truncate()
target.write(json.dumps(outJson))
target.close()
target = open(outfile, 'w')
target.truncate()
target.write(json.dumps(tagdata))
target.close()
print 'Done....'


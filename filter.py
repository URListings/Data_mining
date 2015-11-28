import sys
import json
import csv

filename = sys.argv[1]
removeFields = sys.argv[2]
outfile = sys.argv[3]
outfileJson = outfile + 'dict.json'
with open(filename) as data_file:    
    data = json.load(data_file)
tagdata = []
outJson = {}
removeFields = removeFields.split(",")
for proj in data:
 tags = proj['tags'] 
 if tags is not None:
   for f in removeFields:
     del proj[f]
   outJson[proj['url']] = proj
   tagdata.append(proj)
target = open(outfileJson, 'w')
target.truncate()
target.write(json.dumps(outJson))
target.close()
target = open(outfile, 'w')
target.truncate()
target.write(json.dumps(tagdata))
target.close()
print 'Done....'

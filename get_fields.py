import sys
import json
import csv

filename = sys.argv[1]
fileout = sys.argv[2]

with open(filename) as data_file:    
    data = json.load(data_file)
tagdata = []
for proj in data:
 tags = proj['tags']
 del proj['class_name']
 del proj['has_video']
 del proj['slug']
 if tags is not None:
   tags.sort()
   tagdata.append(tags)
with open(fileout, 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(tagdata)
target = open(filename, 'w')
target.truncate()
target.write(json.dumps(data))
target.close()
print 'Done....'
target.close

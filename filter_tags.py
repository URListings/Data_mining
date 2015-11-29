import sys
import json
import csv

filename = sys.argv[1]
fileout = sys.argv[2]


with open(filename) as data_file:    
    data = json.load(data_file)
tagdata = []
maxLen = 0
for proj in data:
 tags = proj['tags']
 tags.sort()
 tagdata.append(tags)
with open(fileout, 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(tagdata)
print 'Done....'

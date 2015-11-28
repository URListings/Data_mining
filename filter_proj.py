import sys
import json
import csv

filename = sys.argv[1]
fileout = sys.argv[2]


with open(filename) as data_file:    
    data = json.load(data_file)
tagdata = []
tags_map = {}
maxLen = 0
for proj in data:
 maxLen = max(len(proj['tags']), maxLen)
 for s in proj['tags']:
   tags_map[s] = 1
tag_header = []
for key in tags_map:
  tag_header.append(key)
tag_header.sort()
print maxLen
i = 1
while i <= maxLen:
 tag_header.append(i)
 i += 1
tagdata.append(tag_header)
for proj in data:
 i = len(proj['tags'])
 tags = proj['tags']
 tags.sort()
 while i <= maxLen:
  tag_header.append(i)
  i += 1
 tagdata.append(tags)
with open(fileout, 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(tagdata)
print 'Done....'

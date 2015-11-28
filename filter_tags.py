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
 maxLen = max(len(proj['tags']), maxLen)
tag_header = []
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
 while i < maxLen:
  tags.append('')
  i += 1
 tagdata.append(tags)
with open(fileout, 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(tagdata)
print 'Done....'

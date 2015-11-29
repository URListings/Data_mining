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
 for s in proj['tags']:
   if s not in tags_map:
    tags_map[s] = 1
   else:
    tags_map[s] += 1
tag_header = []
print len(tags_map)
for key in tags_map:
  count = tags_map[key]
  if count > 200:
   tag_header.append(key)
tag_header.sort()
tagdata.append(tag_header)
i = 1
print len(tag_header)
for proj in data:
 tags = proj['tags']
 tags.sort()
 tag_dic = {}
 row = []
 insert = 0
 for s in tags:
   tag_dic[s] = 1
 for s in tag_header:
   if s in tag_dic:
     row.append('True')
     insert = 1
   else:
     row.append('False')
 if insert == 1:
  tagdata.append(row)
with open(fileout, 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(tagdata)
print 'Done....'

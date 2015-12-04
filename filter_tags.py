import sys
import json
import csv
import os

filename = sys.argv[1]
fileout = sys.argv[2]
arg_type = sys.argv[3]
if not os.path.exists(os.path.dirname(fileout)):
    os.makedirs(os.path.dirname(fileout))

def tags_with_true():
 winner = 'user_wins_comp'
 min_freq_count = int(sys.argv[4])
 with open(filename) as data_file:    
     data = json.load(data_file)
 tagdata = []
 tags_map = {}
 maxLen = 0
 print 'Projects count:' + str(len(data))
 for proj in data:
  if proj['tags'] is None:
    continue 
  for s in proj['tags']:
    if s not in tags_map:
     tags_map[s] = 1
    else:
     tags_map[s] += 1
 tag_header = []
 print 'Total tags:' + str(len(tags_map))
 for key in tags_map:
   count = tags_map[key]
   if count > min_freq_count:
    tag_header.append(key)
 tag_header.sort()
 tag_header.append(winner)
 tagdata.append(tag_header)
 i = 0
 tagged_proj = 0
 tagged_proj_included = 0
 print 'Filtered tags:' + str(len(tag_header))
 for proj in data:
  tags = proj['tags']
  if tags is None:
    continue
  tagged_proj += 1
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
    elif s == winner:
      if proj['winner'] == True and insert == 1:
        i += 1
      row.append(str(proj['winner'])) 
    else:
      row.append('?')
  if insert == 1:
   tagged_proj_included += 1
   tagdata.append(row)
 print 'Project with tags:' + str(tagged_proj)
 print 'Projects included:' + str(tagged_proj_included)
 print 'Winners:' + str(i)
 with open(fileout, 'wb') as fp:
     a = csv.writer(fp, delimiter=',')
     a.writerows(tagdata)
 print 'Done....'

def tags_with_userGroup():
 winner = 'user_wins_comp'
 other = ['members', 'hack_count','proj_count','avg_exp']
 min_freq_count = int(sys.argv[4])
 user_file = sys.argv[5]
 with open(filename) as data_file:    
     data = json.load(data_file)
 with open(user_file) as data_file:    
     userDic = json.load(data_file)
 tagdata = []
 tags_map = {}
 maxLen = 0
 print 'Projects count:' + str(len(data))
 for proj in data:
  if proj['tags'] is None:
    continue 
  for s in proj['tags']:
    if s not in tags_map:
     tags_map[s] = 1
    else:
     tags_map[s] += 1
 tag_header = []
 print 'Total tags:' + str(len(tags_map))
 for key in tags_map:
   count = tags_map[key]
   if count > min_freq_count:
    tag_header.append(key)
 tag_header.sort()
 tag_header.append(winner)
 tagdata.append(tag_header)
 i = 0
 tagged_proj = 0
 tagged_proj_included = 0
 print 'Filtered tags:' + str(len(tag_header))
 for proj in data:
  tags = proj['tags']
  if tags is None:
    continue
  tagged_proj += 1
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
    elif s == winner:
      if proj['winner'] == True and insert == 1:
        i += 1
      row.append(str(proj['winner'])) 
    else:
      row.append('?')
  if insert == 1:
   members = proj['members']
   members_count = 1 if members is None else len(members)
   hack_count = 1  
   proj_count = 1
   avg_exp = 1
   if members is not None:
      for m in members:
        if m in userDic:
          hack_count += int(userDic[m]['hackathons_count'])
          proj_count += int(userDic[m]['projects_count'])
   avg_exp = max(hack_count, proj_count)/members_count
   row.append(members_count)
   row.append(hack_count)
   row.append(proj_count)
   row.append(avg_exp)
   tagged_proj_included += 1
   tagdata.append(row)
 print 'Project with tags:' + str(tagged_proj)
 print 'Projects included:' + str(tagged_proj_included)
 print 'Winners:' + str(i)
 tag_header.extend(other)
 tagdata[0] = tag_header
 with open(fileout, 'wb') as fp:
     a = csv.writer(fp, delimiter=',')
     a.writerows(tagdata)
 print 'Done....'

def tags_csv():
 with open(filename) as data_file:    
    data = json.load(data_file)
 tagdata = []
 maxLen = 0
 for proj in data:
  tags = proj['tags']
  if tags is None:
    continue
  tags.sort()
  tagdata.append(tags)
 with open(fileout, 'wb') as fp:
    a = csv.writer(fp, delimiter=',')
    a.writerows(tagdata)
 print 'Done....'


if arg_type == '1':
 tags_csv()
elif arg_type == '3':
 tags_with_userGroup()
else:
 tags_with_true()

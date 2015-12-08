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
      row.append('1')
      insert = 1
    else:
      row.append('0')
  if insert == 1:
   if proj['winner'] == True:
      i += 1
   #row.append(str(proj['winner']))
   tagged_proj_included += 1
   tagdata.append(row)
 #tag_header.append(winner)
 print 'Project with tags:' + str(tagged_proj)
 print 'Projects included:' + str(tagged_proj_included)
 print 'Winners:' + str(i)
 with open(fileout, 'wb') as fp:
     a = csv.writer(fp, delimiter=',')
     a.writerows(tagdata)
 print 'Done....'

def tags_with_userGroup():
 other = ['members', 'hack_count','proj_count','avg_exp','user_wins_comp']
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
    else:
      row.append('?')
  if insert == 1:
   members = proj['members']
   members_count = 1 if members is None else len(members)
   if members_count >=4:
	members_count = 4
   hack_count = 1  
   proj_count = 1
   avg_exp = 1
   if members is not None:
      for m in members:
        if m in userDic:
          hack_count += int(userDic[m]['hackathons_count'])
          proj_count += int(userDic[m]['projects_count'])
   hack_count = hack_count if hack_count <=10 else 10  
   proj_count = proj_count if proj_count <=10 else 10
   avg_exp = max(hack_count, proj_count)/members_count
   row.append(members_count)
   row.append(hack_count)
   row.append(proj_count)
   row.append(avg_exp)
   if proj['winner'] == True:
     i += 1
   row.append(str(proj['winner']))
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

def getWinnerTagsCount():
 with open(filename) as data_file:    
    data = json.load(data_file)
 tagdata = {}
 out = ''
 for proj in data:
  if proj['winner'] == False:
    continue
  tags = proj['tags']
  if tags is not None: 
   for f in tags:
    if f in tagdata:
      tagdata[f] += 1
    else:
      tagdata[f] = 1

 for key in tagdata:
   if tagdata[key] > 20:
     out = out + key + ';' + str(tagdata[key]) + '\n'
 with open(fileout, 'wb') as fp:
    fp.write(out)
 print 'Done....'

def getAllTags():
 with open(filename) as data_file:    
    data = json.load(data_file)
 tagdata = {}
 out = ''
 for proj in data:
  tags = proj['tags']
  if tags is not None: 
   for f in tags:
    if f in tagdata:
      tagdata[f] += 1
    else:
      tagdata[f] = 1

 for key in tagdata:
   if tagdata[key] > 100:
     out = out + key + ';' + str(tagdata[key]) + '\n'
 with open(fileout, 'wb') as fp:
    fp.write(out)
 print 'Done....'


def getScatterPlotData():
 threshold = int(sys.argv[4])
 with open(filename) as data_file:    
    data = json.load(data_file)
 tagdata = [['Tag','Project_count' ,'Win_count','Win:Proj']]
 tagkey = {}
 for proj in data:
  tags = proj['tags']
  if tags is not None: 
   for f in tags:
    if f in tagkey:
       arr = tagkey[f]
       arr[1] += 1
       if proj['winner'] == True:
         arr[2] += 1
    else:
      arr = []
      arr.extend([f, 0, 0])
      tagkey[f] = arr
 for key in tagkey:
   arr = tagkey[key]
   if arr[1] > threshold:
     arr.append(round(float(arr[2])/arr[1], 4))
     tagdata.append(arr)
 with open(fileout, 'wb') as fp:
     a = csv.writer(fp, delimiter=',')
     a.writerows(tagdata)
 print 'Done....'


if arg_type == '1':
 tags_csv()
elif arg_type == '3':
 tags_with_userGroup()
elif arg_type == '4':
 getAllTags()
elif arg_type == '5':
 getWinnerTagsCount()
elif arg_type == '6':
 getScatterPlotData()
else:
 tags_with_true()

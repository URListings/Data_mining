import cStringIO
import sys
import json
import csv

state_dict = {'Mississippi': 'Mississippi', 'Oklahoma': 'Oklahoma', 'Delaware': 'Delaware', 'Minnesota': 'Minnesota', 'Illinois': 'Illinois', 'Arkansas': 'Arkansas', 'New Mexico': 'New Mexico', 'Indiana': 'Indiana', 'Maryland': 'Maryland', 'Louisiana': 'Louisiana', 'Idaho': 'Idaho', 'Wyoming': 'Wyoming', 'Tennessee': 'Tennessee', 'Arizona': 'Arizona', 'Iowa': 'Iowa', 'Michigan': 'Michigan', 'Kansas': 'Kansas', 'Utah': 'Utah', 'Virginia': 'Virginia', 'Oregon': 'Oregon', 'Connecticut': 'Connecticut', 'Montana': 'Montana', 'California': 'California', 'Massachusetts': 'Massachusetts', 'West Virginia': 'West Virginia', 'South Carolina': 'South Carolina', 'New Hampshire': 'New Hampshire', 'Wisconsin': 'Wisconsin', 'Vermont': 'Vermont', 'Georgia': 'Georgia', 'North Dakota': 'North Dakota', 'Pennsylvania': 'Pennsylvania', 'Florida': 'Florida', 'Alaska': 'Alaska', 'Kentucky': 'Kentucky', 'Hawaii': 'Hawaii', 'Nebraska': 'Nebraska', 'Missouri': 'Missouri', 'Ohio': 'Ohio', 'Alabama': 'Alabama', 'New York': 'New York', 'South Dakota': 'South Dakota', 'Colorado': 'Colorado', 'New Jersey': 'New Jersey', 'Washington': 'Washington', 'North Carolina': 'North Carolina', 'District of Columbia': 'District of Columbia', 'Texas': 'Texas', 'Nevada': 'Nevada', 'Maine': 'Maine', 'Rhode Island': 'Rhode Island'}
state_abbrv_dict = {'WA': 'Washington', 'DE': 'Delaware', 'DC': 'District of Columbia', 'WI': 'Wisconsin', 'WV': 'West Virginia', 'HI': 'Hawaii', 'FL': 'Florida', 'WY': 'Wyoming', 'NH': 'New Hampshire', 'NJ': 'New Jersey', 'NM': 'New Mexico', 'TX': 'Texas', 'LA': 'Louisiana', 'NC': 'North Carolina', 'ND': 'North Dakota', 'NE': 'Nebraska', 'TN': 'Tennessee', 'NY': 'New York', 'PA': 'Pennsylvania', 'CA': 'California', 'NV': 'Nevada', 'VA': 'Virginia', 'CO': 'Colorado', 'AK': 'Alaska', 'AL': 'Alabama', 'AR': 'Arkansas', 'VT': 'Vermont', 'IL': 'Illinois', 'GA': 'Georgia', 'IN': 'Indiana', 'IA': 'Iowa', 'MA': 'Massachusetts', 'AZ': 'Arizona', 'ID': 'Idaho', 'CT': 'Connecticut', 'ME': 'Maine', 'MD': 'Maryland', 'OK': 'Oklahoma', 'OH': 'Ohio', 'UT': 'Utah', 'MO': 'Missouri', 'MN': 'Minnesota', 'MI': 'Michigan', 'RI': 'Rhode Island', 'KS': 'Kansas', 'MT': 'Montana', 'MS': 'Mississippi', 'SC': 'South Carolina', 'KY': 'Kentucky', 'OR': 'Oregon', 'SD': 'South Dakota'}


def checkUS(c):
  return c.find('US') > -1 or c.find('United States') > -1

def getLocationsJson(filename):
  print filename
  with open(filename) as data_file:    
    data = data_file.read()
  content = data.split('\n')
  other = 0
  states_count = {}
  for key in state_dict:
    states_count[key] = 0
  for c in content:
    found = False
    key = ''
    loc_arr = c.split(",")
    for val in loc_arr:
      key = val.strip()
      if key in state_dict:
        found = True
        if c.lower().find('district of columbia') > -1:
           key = 'District of Columbia'
        break
      elif key in state_abbrv_dict:
        found = True
        key = state_abbrv_dict[key]
        break
    if found and (checkUS(c) or len(loc_arr) == 1):
       states_count[key] += 1
    else:
       other += 1
  actual_count = 0
  for key in states_count:
    actual_count += states_count[key]
  print "US count:" + str(actual_count)
  print "Other locations:" + str(other)
  print "Total locations:" + str(len(content))
  print states_count
  print 'Done....'
  return states_count


file_all_loc = sys.argv[1]
file_winner_loc = sys.argv[2]
file_out = sys.argv[3]
participant_json = sys.argv[4]
print "-------------------All states --------------------"
all_states = getLocationsJson(file_all_loc)
print "-------------------Winners states --------------------"
winner_by_states = getLocationsJson(file_winner_loc)
tagdata = [["state", "participant_count", "win_count", "win_ratio"]]
for key in all_states:
  participants = all_states[key]
  winners = winner_by_states[key]
  ratio = 0 if participants < 50 else float(winners)/participants
  row = [key, participants, winners, ratio]
  tagdata.append(row)

with open(file_out, "wb") as fp:
  a = csv.writer(fp, delimiter=',')
  a.writerows(tagdata)
states_hackData = 'var states_hackData = ' + str(all_states) + ';'
with open(participant_json, 'wb') as fp:
  fp.write(states_hackData)





import pycurl
import cStringIO
import sys
import json
from pprint import pprint

filename = sys.argv[1]
fileout = sys.argv[2]
target = open(fileout, 'wb')
progress = open('progress.txt', 'wb')
target.truncate()
c = pycurl.Curl()
errorMessage = 'errorMessage'
def getUserInfo(userId):
  i = 1
  while i <=1:
    link = 'https://iii3mdppm7.execute-api.us-east-1.amazonaws.com/prod/UserPortfolioEndpoint/'+userId
    c.setopt(pycurl.URL, link)
    buf = cStringIO.StringIO()
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    resp = buf.getvalue()
    resp = json.loads(resp)
    if errorMessage in resp:
      i += 1
    else:
      del resp['projects']
      del resp['bio']
      resp['skill'] = []
      if resp['specializations'] is not None:
        spe = resp['specializations']
        for obj in spe:
          resp['skill'].append(obj['name'])
        del resp['specializations']
      return resp 
  return resp

with open(filename) as data_file:    
    data = json.load(data_file)
users = {}
for proj in data:
 members = proj['members']
 if members is not None:
  for user in members:
   users[user] = 1
data = []
target.write('[')
size = len(users)
print size
i = 1
err_count = 0
progress.write('\n Total user count:'+str(size))
for key in users:
  try:
    resp = getUserInfo(key.strip())
  except Exception:
    progress.write('\nError for the user:' + key)
    excep = True
    
  if screenName not in resp or excep == True:
    err_count += 1
    continue
  else:
    if(i != 1):
     target.write(',')
    target.write(json.dumps(resp))
  i = i + 1
  if i % 300 == 0:
    progress.write(str(i) + ',\n')
  progress.flush()
target.write(']')
progress.write('\n Total error count:'+str(err_count))
print 'Done....'
target.close()
progress.close()

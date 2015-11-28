import pycurl
import cStringIO
import sys
import json
from pprint import pprint

filename = sys.argv[1]
fileout = sys.argv[2]
target = open(fileout, 'w')
target.truncate()
c = pycurl.Curl()

def getUserInfo(userId):
  i = 1
  while i <=3:
    link = 'https://iii3mdppm7.execute-api.us-east-1.amazonaws.com/prod/UserPortfolioEndpoint/'+userId
    c.setopt(pycurl.URL, link)
    buf = cStringIO.StringIO()
    c.setopt(c.WRITEFUNCTION, buf.write)
    c.perform()
    resp = buf.getvalue()
    if resp[2:14] != 'errorMessage':
      return resp
    i += 1
  return 'error'


with open(filename) as data_file:    
    data = json.load(data_file)
users = {}
for proj in data:
 members = proj['members']
 if members is not None:
  for user in members:
   users[user] = 1
data = None
target.write('[')
size = len(users)
print size
i = 1
for key in users:
  resp = getUserInfo(key)
  if resp != 'error':
    if(i < size):
      resp += ','
    target.write(resp)
  i = i + 1
target.write(']')
print 'Done....'
target.close

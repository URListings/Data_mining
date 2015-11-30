import pycurl
import cStringIO
import sys

filename = sys.argv[1]
query = sys.argv[3]
target = open(filename, 'w')
target.truncate()

total = int(sys.argv[2])
pagesize = 6
page = total/pagesize

if(total % pagesize > 0):
 page += 1
i = 1
query = sys.argv[1]
if query == 'full':
  query = ''
c = pycurl.Curl()
target.write('[')
while(i <= page):
  link = 'http://devpost.com/software/search.json?query='+query+'&page=' + str(i)
  c.setopt(pycurl.URL, link)
  buf = cStringIO.StringIO()
  c.setopt(c.WRITEFUNCTION, buf.write)
  c.perform()
  resp = buf.getvalue()
  append = resp[resp.find('[') + 1:resp.rfind(']')]
  if(i < page):
    append += ','
  target.write(append)
  i = i + 1
target.write(']')
print 'Done....'
target.close


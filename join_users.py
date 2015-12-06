import pycurl
import cStringIO
import sys
import json
from pprint import pprint

file1 = sys.argv[1]
file2 = sys.argv[2]
fileout = sys.argv[3]

with open(file1) as data_file:    
    data1 = json.load(data_file)
with open(file2) as data_file:    
    data2 = json.load(data_file)


print '\n Total file1 count:'+str(len(data1))
print '\n Total file2 count:'+str(len(data2))

data1.extend(data2)

print '\n New file1 count:'+str(len(data1))

target = open(fileout, 'w')
target.truncate()
target.write(json.dumps(data1))
target.close()

print 'Done....'

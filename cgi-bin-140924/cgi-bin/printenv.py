#c:/python34/python.exe
#import sys
import os
import re

print ("Content-Type: text/plain; charset=UTF-8")
print()

print ("<h1>Hello!</h1>")

"""
info about the device
return list of tuple: example, Username bango_000
"""
for (k,v) in os.environ.items() :
 print (k, v)

print ()
print ("==========================")
print ()

x = os.environ['QUERY_STRING'] #? info, pathname of directory
print ("Query is ", x)
comps = re.split('&', x) #split word from &
for c in comps:
    print (c)
    (key, val) = re.split('=', c) #?
    print (key,'--->',val)

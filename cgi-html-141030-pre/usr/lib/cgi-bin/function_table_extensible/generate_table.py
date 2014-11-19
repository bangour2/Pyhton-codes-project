#!/usr/bin/python3

__author__ = 'student'


import cgi
import cgitb
cgitb.enable()
from function_table_extensible.error_page import page
import math
from jinja2 import Environment, FileSystemLoader
from function_table_extensible.Functions import getFunctionByKey

print("Content-Type: text/html; charset=UTF-8")
print("")



fldstor = cgi.FieldStorage()

start = float(fldstor.getfirst('start', 0.1))
end = float(fldstor.getfirst('end',10))
numrows = int(fldstor.getfirst('numrow', 20))
function_key_list = fldstor.getlist('function')

header_list = ['x']
for fk in function_key_list:
    func = getFunctionByKey(fk)
    if func :
        header_list.append(func.header)
    #else:
    #    header_list.append("error")


#if start < .1:
#    page("Start value must be greater than .1")
#    quit()

if start > end:
   page("Start value should be less than end", "Back up and try again")
   quit()

if numrows < 2:
    page("The number of rows must be at least 2")
    quit()

step = (end - start)/(numrows-1)  # step in x between rows


# body
data = []
for row in range(0,numrows):
    x = start + row * step

    rowdata = [x]
    for fkey in function_key_list:
        try:
            func = getFunctionByKey(fkey)
            if func:
                rowdata.append(func.compute(x))
            #else:
        except ValueError:
            rowdata.append('error')

    data.append(rowdata)

#print(function_list)

#print(data)

ldr = FileSystemLoader('templates')
env = Environment(loader=ldr)
tmplt = env.get_template('func_tab.html')
rndrd = tmplt.render(headers=header_list, data=data)
print(rndrd)




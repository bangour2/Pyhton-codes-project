#!/usr/bin/python3

__author__ = 'student'


import cgi
import cgitb
cgitb.enable()
from function_table_with_templates.error_page import page
import math
from jinja2 import Environment, FileSystemLoader

print("Content-Type: text/html; charset=UTF-8")
print("")



fldstor = cgi.FieldStorage()

start = float(fldstor.getfirst('start', 0.1))
end = float(fldstor.getfirst('end',10))
numrows = int(fldstor.getfirst('numrow', 20))
function_list = fldstor.getlist('function')

header_list = ['x'] + function_list

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
    for func in function_list:
        try:
            if func == 'cube':
                rowdata.append(x*x*x)
            elif func == 'square':
                rowdata.append(x*x)
            elif func == 'ln':
                rowdata.append(math.log(x))
            elif func == 'log2':
                rowdata.append(math.log2(x))
            elif func == 'atan':
                rowdata.append(math.atan(x))
            elif func == 'sqrt':
                rowdata.append(math.sqrt(x))
            else:
                rowdata.append('oops')
        except ValueError:
            rowdata.append('error')

    data.append(rowdata)

#print(function_list)

#print(data)

ldr = FileSystemLoader('.')
env = Environment(loader=ldr)
tmplt = env.get_template('func_tab.html')
rndrd = tmplt.render(headers=header_list, data=data)
print(rndrd)




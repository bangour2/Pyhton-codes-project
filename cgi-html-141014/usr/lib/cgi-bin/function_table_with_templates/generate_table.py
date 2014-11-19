#!/usr/bin/python3

__author__ = 'student'


import cgi
import cgitb
cgitb.enable()
from function_table.error_page import page
import math

print("Content-Type: text/html; charset=UTF-8")
print("")


page_top = """
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Function Table</title>
    <link href="/style1.css" rel="stylesheet" type="text/css"/>
</head>
<body>
    <h1>Function Table</h1>
"""

page_bottom = """
</body>
</html>
"""

fldstor = cgi.FieldStorage()

start = float(fldstor.getfirst('start', 0.1))
end = float(fldstor.getfirst('end',10))
numrows = int(fldstor.getfirst('numrow', 20))
function_list = fldstor.getlist('function')

#if start < .1:
#    page("Start value must be greater than .1")
#    quit()

if start > end:
   page("Start value should be less than end", "Back up and try again")
   quit()

if numrows < 2:
    page("The number of rows must be at least 2")
    quit()


#  start printing the generated page
# now we know that the input data is ok

print( page_top)

#print("<p>start", start, "</p>")
#print("<p>end", end, "</p>")
#print("<p>number of rows {}</p>".format(numrows))
#print("<p>functions {}</p>".format(function_list))


step = (end - start)/(numrows-1)  # step in x between rows




print("<table class='grid'>")

print("<tr>")
print("<th>x</th>")
for func in function_list:
    print("<th>", func, "</th>")
print("</tr>")

# body
for row in range(0,numrows):
    x = start + row * step
    cell_template = "<td class='numeric'>{:.3f}</td>"
    print("<tr>")
    print("<th>{:.3f}</th>".format(x))


    for func in function_list:
        try:
            if func == 'cube':
                print(cell_template.format(x*x*x))
            elif func == 'square':
                print(cell_template.format(x*x))
            elif func == 'ln':
                print(cell_template.format(math.log(x)))
            elif func == 'log2':
                print(cell_template.format(math.log2(x)))
            elif func == 'atan':
                print(cell_template.format(math.atan(x)))
            elif func == 'sqrt':
                print(cell_template.format(math.sqrt(x)))

            else:
                print("<td>oops</td>")
        except ValueError:
            print("<td class='error'>err</td>")

    print("</tr>")

print("</table>")




print(page_bottom)

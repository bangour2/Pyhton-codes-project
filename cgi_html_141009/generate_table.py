#!C:\Python34\python.exe
__author__ = 'student'

import cgi
import cgitb
cgitb.enable()


from cgi_html_141009.error_page import page

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

fldstor = cgi.FieldStorage()#?

start = float(fldstor.getfirst('start', 0.1))
end = float(fldstor.getfirst('end',10))
numrows = float(fldstor.getfirst('numrow', 20))
function_list = fldstor.getlist('function')

if start < .1:
    page("Start value must be greater than .1")
    quit()

if start > end:
   page("Start value should be less than end")
   quit()

if numrows < 2:
    page("The number of rows must be at least 2")
    quit()

print( page_top)

print("<p>start", start, "</p>")
print("<p>end", end, "</p>")
print("<p>number of rows {}</p>".format(numrows))#?
print("<p>functions {}</p>".format(function_list))


step = (end - start)/(numrows-1)  # step in x between rows




print("<table>")


print("</table>")




print(page_bottom)

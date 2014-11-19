#!/usr/bin/python3
#import sys
import os
import re
import sys
import cgitb
cgitb.enable()

print ("Content-Type: text/html; charset=UTF-8")
print ("")

first  = """
<!DOCTYPE html>
<html>
<head>
 <title>Query Reflection</title>
 <link rel="Stylesheet" type="text/css" href="/style1.css"/>
</head>
<body>
""" 
last = """
</body>
</hthml>
"""

print(first)
print ("<h1>Query Reflection</h1>")
 
 
x = os.environ['QUERY_STRING']
print ("<p>Query is ", x, "</p>")

if True:
	comps = re.split('&', x)
	print("<table>")
	for c in comps:
		rowpic = "<tr><td>{}</td><td>{}</td></tr>"
		(key, val) = re.split('=', c)
		print(rowpic.format(key,val))
	print("</table>")
	

print ("<h1>Body</h1>")

body = sys.stdin.readlines() # reads multiple lines, but there is at most one

print("<p>Body is ",body,"</p>")

if body:
	body = body[0]
	comps = re.split('&', body)
	print("<table>")
	for c in comps:
		rowpic = "<tr><td>{}</td><td>{}</td></tr>"
		(key, val) = re.split('=', c)
		print(rowpic.format(key,val))
	print("</table>")
	

print(last)
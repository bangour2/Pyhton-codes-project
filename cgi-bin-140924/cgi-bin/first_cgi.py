#!/usr/bin/python3
#c:/python34/python.exe

import os

__author__ = 'Ben Setzer'


print("Content-Type: text/html; charset=UTF-8")
print("")

print("<h1>Hello World!</h1>")

print("<h2>Line breaks</h2>")

for (k,v) in os.environ.items() :
     print(k, v, "<br />")


print("<h2>Table</h2>")

print("<table>")
for (k,v) in os.environ.items() : # device information
     #print("<tr><td>",k, "</td><td>",v, "</td></tr>")
     row = "<tr><td>%s</td><td>%s</td></tr>"%(k,v) #variable, value
     print(row)

print("</table")

print("<h2>Preformatted</h2>")

print("<pre>")
for (k,v) in os.environ.items() :
     print(k, v)
print("</pre>")
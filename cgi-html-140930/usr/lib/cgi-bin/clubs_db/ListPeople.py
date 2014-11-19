#!/usr/bin/python3
import psycopg2

__author__ = 'Ben Setzer'
'''
    List all people in the clubs database
'''


print("Content-Type: text/html; charset=UTF-8")
print("")


conn = psycopg2.connect(database="clubs", user="clubs", password="clubs", host="localhost")

get_people_cmd = "select ident, name, email from person"
crs = conn.cursor()
crs.execute(get_people_cmd)

print("<table>")
for p in crs:
    row_fmt = "<tr><td>{1:15s}</td><td>{2:30s}</td><td>{0:5d}</td></tr>"
    #row = row_fmt.format(p[0], p[1], p[2])
    row = row_fmt.format(*p)
    print(row)
print("</table>")


conn.close()




#!/usr/bin/python3
import psycopg2

__author__ = 'Ben Setzer'
'''
    List all people in the clubs database
'''

conn = psycopg2.connect(database="clubs", user="clubs", password="clubs", host="localhost")

get_people_cmd = "select ident, name, email from person"
crs = conn.cursor()
crs.execute(get_people_cmd)

for p in crs:
    row_fmt = "{1:15s}   {2:30s}    {0:5d}"
    #row = row_fmt.format(p[0], p[1], p[2])
    row = row_fmt.format(*p)
    print(row)

print("=================")

for col in crs.description:
    print(col)

print("=================")

for p in crs:
    print(p)

print("=================")


# get again

crs.execute(get_people_cmd)

list =  crs.fetchall()
for p in list:
    print(p)
for p in list:
    print(p)


print("=================")

crs.execute(get_people_cmd)

one = crs.fetchone()

print(one)

print("=================")


conn.close()




#!/usr/bin/python3
#  c:/python34/python.exe
#  c:/python34/py.exe
import psycopg2
import os

__author__ = 'Ben Setzer'

'''
    Get a person for a given id.
'''

print("Content-Type: text/plain; charset=UTF-8")
print("")

conn = psycopg2.connect(database="clubs", user="clubs", password="clubs", host="localhost")
crs = conn.cursor()

id = 103 #  Carol's id

get_person_cmd = "select ident, name, email from person where ident = " + str(id)

crs.execute(get_person_cmd)

print("Number of rows: " + str(crs.rowcount))

person = crs.fetchone()

print("Person is {}".format(person))

############################################


id = 103 #  Carol's id

get_person_cmd = "select ident, name, email from person where ident = %s"

crs.execute(get_person_cmd, (id,))


print("Number of rows: " + str(crs.rowcount))

person = crs.fetchone()

print("Person is {}".format(person))


print("-=================")
qs = os.environ["QUERY_STRING"]
print("Query string is",qs)

# parse the string to get the id
# continue as above


conn.close()

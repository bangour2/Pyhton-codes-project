#!/usr/bin/python3

__author__ = 'student'

# list the data about one person

import cgitb
cgitb.enable()
from jinja2 import Environment, FileSystemLoader
import sqlite3
import cgi
from clubs_db3_sqlite import error_page
from clubs_db3_sqlite.db import get_connection

fldr = FileSystemLoader("templates")
jenv = Environment(loader=fldr)

fldstor = cgi.FieldStorage()
idlist = fldstor.getlist("id")

if len(idlist) != 1:
    error_page.page("A single id was not provided to the program")
    quit()

try:
    person_id = int(idlist[0])
except ValueError as ve:
    error_page.page("Invalid person Id presented: %s" % idlist[0],
                    "Return to the table of people and make the choice agains")
    quit()


conn = get_connection()
cur = conn.cursor()
cmd = "select name, email from person where ident = ?"
cur.execute(cmd, (person_id,))

personList = cur.fetchall()

if len(personList) != 1:
    error_page.page("Id %d does not match any person in the database" % person_id)

person = personList[0]


print("Content-Type: text/html; charset=UTF-8")
print("")

template = jenv.get_template("ListOnePerson.html")
template_rendered = template.render(person=person)
print(template_rendered)

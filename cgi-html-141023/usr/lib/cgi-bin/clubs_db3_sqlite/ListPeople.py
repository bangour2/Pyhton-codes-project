#!/usr/bin/python3

__author__ = 'student'


import cgitb
cgitb.enable()
from jinja2 import Environment, FileSystemLoader
#import psycopg2
import sqlite3

print("Content-Type: text/html; charset=UTF-8")
print("")


#conn = psycopg2.connect(database="clubs", user="clubs", password="clubs", host="localhost")
conn = sqlite3.connect("clubs.db")
crs = conn.cursor()
cmd = 'select name, ident, email from person'
crs.execute(cmd)

result = crs.fetchall()

#print(result)

ldr = FileSystemLoader("templates")
env = Environment(loader=ldr)
template = env.get_template("List_Information.html")
template_rendered = template.render(result_list=result)

print(template_rendered)
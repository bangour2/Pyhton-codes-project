#!/usr/bin/python3

__author__ = 'student'



import cgi
import cgitb
cgitb.enable()
from function_table_extensible.error_page import page
import math
from jinja2 import Environment, FileSystemLoader
from function_table_extensible.Functions import function_list


# start the http response
print("Content-Type: text/html; charset=UTF-8")
print("")


#  get Jinja2 environment
ldr = FileSystemLoader('templates')
env = Environment(loader=ldr)
template = env.get_template("function_table_extensible.html")
template_rendered = template.render(function_list=function_list)
print(template_rendered)
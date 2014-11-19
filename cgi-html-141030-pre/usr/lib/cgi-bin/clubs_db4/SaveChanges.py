#!/usr/bin/python3

__author__ = 'student'


import cgi
import cgitb
cgitb.enable()

fldstor = cgi.FieldStorage()
identList = fldstor.getlist('ident')
person_name_list = fldstor.getlist('person-name')
person_email_list = fldstor.getlist('person-email')
club_member_list = fldstor.getlist('club-member')


# validating

# identifier must be unique, numeric and correspond to a real person

# name, email:
#    present --->  update the database
#    not present --->  ignore or raise an error
#           We'll raise an error since the user should be using our page and that will submit
#           both of those

# clubs
#   empty list, no clubs ---> drop from all clubs
#    --. ..






print("Content-Type: text/plain; charset=UTF-8")
print("")

print(identList)
print(person_name_list)
print(person_email_list)
print(club_member_list)


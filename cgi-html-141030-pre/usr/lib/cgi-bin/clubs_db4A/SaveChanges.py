#!/usr/bin/python3
from sqlite3 import IntegrityError

__author__ = 'student'


import cgi
import cgitb
cgitb.enable()
from clubs_db4A import error_page
from clubs_db4A import db
from clubs_db4A import ListOnePerson

fldstor = cgi.FieldStorage()
identList = fldstor.getlist('ident')
person_name_list = fldstor.getlist('person-name')
person_email_list = fldstor.getlist('person-email')
club_member_list = fldstor.getlist('club-member')


# validating

# identifier must be unique, numeric and correspond to a real person


# get id from the query
fldstor = cgi.FieldStorage()
identList = fldstor.getlist("ident")


# check that ident defines a unique value
if len(identList) != 1:
    error_page.page("Exactly one person's identifier should be provided",
                    "Return to the person selection page and try again")
    quit()

try:
    ident = int(identList[0])
except ValueError as ve:
    error_page.page("The identifier for the person must be an integer",
                    str(ve))
    quit()


conn = db.get_connection()
curs = conn.cursor()
cmd = "select name, email from person where ident = ?"
curs.execute(cmd, (ident,))
resultList = curs.fetchall()

if len(resultList) == 0:
    error_page.page("There was no person with this identifier: %d" % ident)
    quit()

person = resultList[0] ## tuple with information about the selected person



# name, email:
#    present --->  update the database
#    not present --->  ignore or raise an error
#           We'll raise an error since the user should be using our page and that will submit
#           both of those

if len(person_name_list) != 1:
    error_page.page("Exactly one user name must be submitted with the form")
    quit()

submitted_name = person_name_list[0]

if person[0] != submitted_name:
    # changing the name, check for overlap
    cmd = "select ident from person where name = ?"
    curs.execute(cmd,(submitted_name,))
    temp = curs.fetchall()
    if len(temp) > 0:
        error_page.page("Name already in use, pick another name: " + submitted_name);
        quit()
    # submitted name is a change and it is not already in use
    cmd = "update  person set name = ? where ident = ?"
    curs.execute(cmd, (submitted_name, ident))
    conn.commit()

if len(person_email_list) != 1:
   error_page.page("Exactly one email address must be submitted with the form")
   quit()

submitted_email = person_email_list[0]

if person[1] != submitted_email:
    cmd = "update person set email = ? where ident = ?"
    curs.execute(cmd, (submitted_email, ident))
    conn.commit()


# clubs
#   empty list, no clubs ---> drop from all clubs
#    --. ..

# build list of clubs for which this person will be a member
member_id_list = []

# first those returned from the form
for cid in club_member_list:
    member_id_list.append(int(cid))

# then the clubs for which the person is president
cmd = "select ident from club where president_id = ?"
curs.execute(cmd, [ident])
for c in curs:
    member_id_list.append(c[0])


# Remove all the club memberships for the user
cmd = "delete from member_of where person_id = ?"
curs.execute(cmd,[ident])

# add all the memberships
try:
    for mid in member_id_list:
        cmd = "insert into member_of (club_id, person_id) values(?,?)"
        curs.execute(cmd,[mid, ident])
except IntegrityError as ie:
    error_page.page("Attempt to insert multiple memberships in the same club", str(ie))
    quit()


conn.commit()

conn.close()

ListOnePerson.page("Save was Successful", ident=ident)



#
# print("Content-Type: text/plain; charset=UTF-8")
# print("")
#
# print(identList)
# print(person_name_list)
# print(person_email_list)
# print(club_member_list)
# print(member_id_list)

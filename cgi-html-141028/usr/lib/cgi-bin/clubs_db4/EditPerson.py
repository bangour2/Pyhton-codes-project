#!/usr/bin/python3

__author__ = 'student'

# list the data about one person

import cgi
import cgitb
cgitb.enable()
from jinja2 import Environment, FileSystemLoader
from clubs_db4 import error_page
from clubs_db4 import db

# set up jinja2
fldr = FileSystemLoader("templates")
jenv = Environment(loader=fldr)


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

## we have a unique ident value and it is a valid integer



conn = db.get_connection()
curs = conn.cursor()

#
#  get person data
#

cmd = "select ident, name, email from person where ident = ?"
curs.execute(cmd, (ident,))
resultList = curs.fetchall()

if len(resultList) == 0:
    error_page.page("There was no person with this identifier: %d" % ident)
    quit()

person = resultList[0] ## tuple with information about the selected person


#
# get club memberships
#

#cmd = "select club.ident, club.name from club, member_of where member_of.person_id = ? and member_of.club_id = club.ident"
#curs.execute(cmd, (ident,))
#membershipList = curs.fetchall()

cmd = "select ident, name from club"
curs.execute(cmd)
allClubs = curs.fetchall()

clubInfoList = []

for cl in allClubs:
    info = [cl[0], cl[1]]  # start with ident and name of club
    cmd = "select club_id from member_of where club_id = ? and person_id = ? "
    curs.execute(cmd, (cl[0], ident))
    ismem = curs.fetchall()
    if len(ismem) > 0:
        info.append(1)  # is a member
    else:
        info.append(0)   # is not a member
    clubInfoList.append(info)




# create page
print("Content-Type: text/html; charset=UTF-8")
print("")
template = jenv.get_template("EditPerson.html")
template_rendered = template.render(ident=ident,
                                    person=person,
                                    presidents = [["Canning"], ["4-H"]],
                                    clubs=clubInfoList
                            )
print(template_rendered)

conn.close()



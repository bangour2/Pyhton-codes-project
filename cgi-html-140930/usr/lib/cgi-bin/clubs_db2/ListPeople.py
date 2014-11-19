#c:/python34/python.exe

import psycopg2
import cgitb
cgitb.enable()

__author__ = 'Ben Setzer'
'''
    List all people in the clubs database
'''

print("Content-Type: text/html; charset=UTF-8")
print("")

header = """
<!DOCTYPE html>
<html>
<head lang="en">
    <meta charset="UTF-8">
    <title>Clubs DB List People</title>
    <link rel="stylesheet" type="text/css" href="/style.css" />
                <!--  href references style.css in the same directory with this file
                -->
</head>
<body>
"""


print(header)

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

## do it again but make a list
crs.execute(get_people_cmd)


print("<ul>")
for p in crs:
    print("<li>")
    print(p[1])
    # create a sublist with information about this person
    print("<ul>")
    print("<li>e-mail: ", p[2],"</li>")
    print("<li>ident: ", p[0], "</li>")

    # get clubs
    crs_club = conn.cursor()
    get_club_cmd = """
        select club.name from club, member_of
            where club.ident = member_of.club_id
              and member_of.person_id = %s
        """
    crs_club.execute(get_club_cmd,(p[0],))  # execute with substitution of parameter
    print("<li>Member of: <ul>")
    for c in crs_club:
        print("<li>", c[0], "</li>")
    print("</ul></li>")


    print("</ul>")

    print("</li>")
print("</ul>")

print("</body>")
print("</html>")

conn.close()




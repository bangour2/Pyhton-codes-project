import psycopg2

__author__ = 'Ben Setzer'

'''
    Get a person for a given id.
'''

conn = psycopg2.connect(database="clubs", user="clubs", password="clubs", host="localhost")
crs = conn.cursor()

id = 103 #  Carol's id

get_person_cmd = "select ident, name, email from person where ident = " + str(id)

crs.execute(get_person_cmd)

print("Number of rows: " + str(crs.rowcount))

person = crs.fetchone() # one row

print("Person is {}".format(person))

############################################


id = 103 #  Carol's id

get_person_cmd = "select ident, name, email from person where ident = %s"

crs.execute(get_person_cmd, (id,))


print("Number of rows: " + str(crs.rowcount))

person = crs.fetchone()

print("Person is {}".format(person))




conn.close()

#!/usr/bin/python3
__author__ = 'Ben'


from clubs_sqlite import databaseSqlite


print("Content-Type: text/html; charset=UTF-8")
print("")



#dumpDB()

people = databaseSqlite.getListOfPeople()
for p in people:
    print(p)


clubs = databaseSqlite.getListOfClubs()
for c in clubs:
    print(c)


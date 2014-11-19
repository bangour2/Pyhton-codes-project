__author__ = 'Ben Setzer'

import clubs
import clubs.club

chad = clubs.Person(102, "Chad", "chad@acme.com") #constructor

print(chad)
for club in chad.memberOf: #list
    print("  ", club)

hhhh = club(103, "4-H", "Agriculture and home economics")

hhhh.members.append(chad)
chad.memberOf.append(hhhh)


print("===================")
print(chad)
for club in chad.memberOf:
    print("  ", club)

ourData = clubs.DataSet(clubs=[hhhh],people=[chad]) #constructor

print("what's in ourData")
print("People")
for p in ourData.people:
    print(p)
print("Clubs")
for c in ourData.clubs:
    print(c)
print("All done")
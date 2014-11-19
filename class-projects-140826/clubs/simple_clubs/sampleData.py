'''
Created on Aug 11, 2013

@author: Ben
'''


import clubs.Person, clubs.Club, clubs.DataSet, clubs.Group

class Sample1(object):



    data = {
        'personNames': ("Alice", "Bob", "Carol", "Dave", "Eve"),
        'personEmails': ("alice@acme.com", "bob@nadir.org", "carol@zenith.net", "dave@acme.com",
                        "eve@nadir.com" ),
        
        
        'clubNames':  ["French", "German", "Rugby", "Field Hockey"],
        'clubDescriptions':  (
                     "Pour les amateurs de la langue francaise",
                     "Diejenigen, die Deutsch sprechen",
                     "Intercollegiate Rugby competition",
                     "Intramural Field Hockey competition"),
        
        'groupNames': ("International", "Sports"),
        'groupDescriptions':  (
                     "Clubs interested in international culture",
                     "Clubs involved with sports"),
                 
        # Position in array is the club.  Value is the person index.
        'presidentOf':  (2,1,0,4),
                 
        # Each pair is (personIndex, clubIndex) indicating that person
        #  is a member of the club
        'member' : (   (0,0), (2,0), (4,0),
                     (1,1), (3,1),
                     (0,2), (1,2), (2,2),
                     (1,3), (3,3), (4,3) ),
         
        # (club, group)
        'inGroup' : (
                     (0,0), (1,0), (2,1), (3,1),
                     (2,0) ),
                
    }
    

def createSample(dataHash):
    '''
        Use a data hash like that above to create a collection
        of objects
    '''
    ds = clubs.DataSet();
    ident = 101

    for i, name in enumerate(dataHash['personNames']): #?
        p = clubs.Person(ident=ident,
                   name=name,
                   e_mail=dataHash['personEmails'][i]) #?
        ident += 1
        ds.people.append(p)
    for i, name in enumerate(dataHash['clubNames']):
        c = clubs.Club(ident=ident,
                 name=name,
                 description=dataHash['clubDescriptions'][i])
        ident += 1
        ds.clubs.append(c)
    for i, name in enumerate(dataHash['groupNames']):
        g = clubs.Group(ident=ident,
                 name=name,
                 description=dataHash['groupDescriptions'][i])
        ident += 1
        ds.groups.append(g)
    for clubI, presI in enumerate(dataHash['presidentOf']):
        club = ds.clubs[clubI]
        pres = ds.people[presI]
        club.president = pres
        pres.presidentOf = club

    # for x in dataHash['member']:
    #     # x is pair of indexes
    #     pass
    #     # x[0] and x[1]

    for pi, ci in dataHash['member']:
        person = ds.people[pi]
        club = ds.clubs[ci]
        person.memberOf.append(club)
        club.members.append(person)
    for ci, gi in dataHash['inGroup']:
        club = ds.clubs[ci]
        group = ds.groups[gi]
        club.groupsIn.append(group)
        group.clubsIn.append(club)
    return ds


def getSample1():
    dsx = createSample(Sample1.data)
    return dsx
    
if __name__ == '__main__':
    print("sample data script")
    dsx = createSample(Sample1.data)
    for p in dsx.people:
        print(p)
        if p.presidentOf:
            print("  Is president of " + p.presidentOf.name)
        for c in p.memberOf:
            print("   member of " + c.name)
    for c in dsx.clubs:
        print(c)
        if c.president:
            print("    President is %s" % c.president.name) #?
        for p in c.members:
            print("    %s is a member" % p.name)
        for g in c.groupsIn:
            print("    belongs to %s" % g.name)
    for g in dsx.groups:
        print(g)
        for c in g.clubsIn:
            print("   Contains %s club " % c.name)
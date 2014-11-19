'''
Created on Aug 11, 2013

Model classes for the clubs example.

@author: Ben
'''

class Person(object):
    '''
        Part of the clubs example
    '''

    def __init__(self,ident,name,e_mail):
        '''
        Constructor
        '''
        self.ident = ident
        self.name = name
        self.e_mail = e_mail
        self.memberOf = []
        self.presidentOf = None


    def __str__(self):
        return "Person[%d  %s  %s]" % (self.ident, self.name, self.e_mail) #?


class Club(object):
    '''
        Part of the clubs example
    '''
    
    def __init__(self,ident, name, description):
        self.ident = ident
        self.name = name
        self.description = description
        self.members = []
        self.groupsIn = []
        self.president = None

    def __str__(self):        
        return "Club[%d  %s -- %s]" % (self.ident, self.name, self.description)

class Group(object):
    '''
        Groups of clubs.
        Part of the clubs example.
    '''
    def __init__(self, ident, name, description):
        self.ident = ident
        self.name = name;
        self.description = description;
        self.clubsIn = []

    def __str__(self):        
        return "Group[%d  %s -- %s]" % (self.ident, self.name, self.description)

class DataSet(object):
    '''
        Holds a list of clubs, a list of
        persons and a list of groups
    '''
    
    def __init__(self, people=[], groups=[], clubs=[]):
        self.people = people
        self.groups = groups
        self.clubs = clubs

    def findPersonById(self, ident):
        for p in self.people:
            if p.ident == ident:
                return p
        return None
    
    
    
    
    
    
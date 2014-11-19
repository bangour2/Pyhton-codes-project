'''
Created on Aug 12, 2013

Database methods for the clubs example

@author: Ben
'''

import sqlite3




def getConnection():
    '''
        Return a connection to the database
    '''
    conn = sqlite3.connect('clubs.db')
    return conn

def getPersonById(ident):
    '''
        Return a tuple with data from the person table for
        the given id.
        Returns in order: ident, name, email
    '''
    conn = getConnection()
    
    cmd = "select ident, name, email from person where ident=?"
    cursor = conn.execute(cmd,(ident,))
    pdata = cursor.fetchone()
    conn.close()
    return pdata

def getListOfPeople():
    '''
        return a list of tuples with information from the
        person database.
        Each tuple is (ident, name, email)
    '''
    conn = getConnection()
    cmd = "select ident, name, email from person"
    cursor = conn.execute(cmd)
    rtval = cursor.fetchall()
    conn.close()
    return rtval


def getGroupById(ident):
    '''
        Return a tuple with data from the group table for
        the given id.
        Returns in order: ident, name, description
    '''
    conn = getConnection()
    
    cmd = "select ident, name, description from `group` where ident=?"
    cursor = conn.execute(cmd,(ident,))
    pdata = cursor.fetchone()
    conn.close()
    return pdata


def getListOfGroups():
    '''
        return a list of tuples with information from the
        group database.
        Each tuple is (ident, name, description)
    '''
    conn = getConnection()
    cmd = "select ident, name, description from `group`"
    cursor = conn.execute(cmd)
    rtval = cursor.fetchall()
    conn.close()
    return rtval


def getClubById(ident):
    '''
        Return a tuple with data from the club table for
        the given id.
        Returns in order: ident, name, description, president_id
    '''
    conn = getConnection()
    
    cmd = "select ident, name, description, president_id from `club` where ident=?"
    cursor = conn.execute(cmd,(ident,))
    pdata = cursor.fetchone()
    conn.close()
    return pdata

def getListOfClubs():
    '''
        return a list of tuples with information from the
        club database.
        Each tuple is (ident, name, description, president_id)
    '''
    conn = getConnection()
    cmd = "select ident, name, description, president_id from club"
    cursor = conn.execute(cmd)
    rtval = cursor.fetchall()
    conn.close()
    return rtval


def savePersonData(pdata):
    '''
        Save the data given in the tuple: (ident, name, email)
    '''
    conn = getConnection()
    
    cmd = 'update person set name = ?, email = ? where ident = ?'
    conn.execute(cmd, (pdata[1], pdata[2], pdata[0]))
    
    conn.commit()
    conn.close()


def saveGroupData(gdata):
    '''
        Save the data given in the tuple: (ident, name, description)
    '''
    conn = getConnection()
    
    cmd = 'update `group` set name = ?, description = ? where ident = ?'
    conn.execute(cmd, (gdata[1], gdata[2], gdata[0]))
    
    conn.commit()
    conn.close()
    
    
    

if __name__ == '__main__':
    pass
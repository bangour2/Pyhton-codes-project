__author__ = 'student'

import sqlite3

def get_connection() :
    return sqlite3.connect("birt.db")


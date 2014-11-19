__author__ = 'student'

import sqlite3

def get_connection():
    conn = sqlite3.connect("clubs.db")
    return conn

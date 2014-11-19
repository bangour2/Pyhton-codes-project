__author__ = 'mohammad'

from Expressions import Expression
from Memory import fetch

class Id (Expression):

    def __init__(self, ch):
        self.ch = ch

    def evaluate(self):
        return fetch (self)

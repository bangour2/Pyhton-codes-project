__author__ = 'mohammad'

from Statements import Statement
from Memory import store

class AssignmentStatement (Statement):

    def __init__(self, var, expr):
        self.var = var
        self.expr = expr

    def execute(self):
        store (self.var, self.expr.evaluate())

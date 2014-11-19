__author__ = 'mohammad'

from Statements import Statement

class PrintStatement (Statement):

    def __init__(self, expr):
        self.expr = expr

    def execute(self):
        print (self.expr.evaluate())

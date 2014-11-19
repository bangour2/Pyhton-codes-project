__author__ = 'mohammad'

from Statements import Statement

class IfStatement (Statement):

    def __init__(self, expr, cb1, cb2):
        self.expr = expr
        self.cb1 = cb1
        self.cb2 = cb2

    def execute(self):
        if self.expr.evaluate():
            self.cb1.execute()
        else:
            self.cb2.execute()

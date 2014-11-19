__author__ = 'mohammad'

from Statements import Statement

class UntilStatement (Statement):

    def __init__(self, expr, cb):
        self.expr = expr
        self.cb = cb

    def execute(self):
        while not self.expr.evaluate():
            self.cb.execute()

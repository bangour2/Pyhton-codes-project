__author__ = 'mohammad'

from Statements import Statement

class WhileStatement (Statement):

    def __init__(self, expr, cb):
        self.expr = expr
        self.cb = cb

    def execute(self):
        while self.expr.evaluate():
            self.cb.execute()

__author__ = 'mohammad'

from Expressions import Expression

class LiteralInteger (Expression):

    def __init__(self, value):
        self.value = value

    def evaluate(self):
        return self.value

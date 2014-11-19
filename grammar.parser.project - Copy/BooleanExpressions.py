__author__ = 'mohammad'

from RelationalOperators import RelationalOperator

class BooleanExpression():

    def __init__(self, op, expr1, expr2):
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        if self.op == RelationalOperator.EQ_OP:
            result = self.expr1.evaluate() == self.expr2.evaluate()
        elif self.op == RelationalOperator.NE_OP:
            result = self.expr1.evaluate() != self.expr2.evaluate()
        elif self.op == RelationalOperator.GE_OP:
            result = self.expr1.evaluate() >= self.expr2.evaluate()
        elif self.op == RelationalOperator.GT_OP:
            result = self.expr1.evaluate() > self.expr2.evaluate()
        elif self.op == RelationalOperator.LT_OP:
            result = self.expr1.evaluate() < self.expr2.evaluate()
        elif self.op == RelationalOperator.LE_OP:
            result = self.expr1.evaluate() <= self.expr2.evaluate()
        else:
            raise IndexError ('boolean expression expected')
        return result

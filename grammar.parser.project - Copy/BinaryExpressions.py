__author__ = 'mohammad'

from Expressions import  Expression
from ArithmeticOperators import ArithmeticOperator

class BinaryExpression (Expression):

    def __init__(self, op, expr1, expr2):
        self.op = op
        self.expr1 = expr1
        self.expr2 = expr2

    def evaluate(self):
        if self.op == ArithmeticOperator.ADD_OP:
            result = self.expr1.evaluate() + self.expr2.evaluate()
        elif self.op == ArithmeticOperator.SUB_OP:
            result = self.expr1.evaluate() - self.expr2.evaluate()
        elif self.op == ArithmeticOperator.MUL_OP:
            result = self.expr1.evaluate() * self.expr2.evaluate()
        elif self.op == ArithmeticOperator.DIV_OP:
            result = self.expr1.evaluate() / self.expr2.evaluate()
        else:
            raise IndexError ('binary expression expected')
        return result



__author__ = 'mohammad'

from IllegalArgumentExceptions import IllegalArgumentException

class Token():

    def __init__(self, row_number, column_number, lexeme,  tok_type):
        if row_number < 0:
            raise IllegalArgumentException ('invalid row number')
        if column_number < 0:
            raise  IllegalArgumentException ('invalid column number')
        if len(lexeme) == 0:
            raise IllegalArgumentException ('invalid lexeme argument')
        self.row_number = row_number
        self.column_number = column_number
        self.lexeme = lexeme
        self.tok_type = tok_type

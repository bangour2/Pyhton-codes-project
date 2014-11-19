__author__ = 'mohammad'


class ParserException (Exception):

    def __init__(self, message):
        self.message = message

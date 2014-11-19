__author__ = 'mohammad'

class Program ():

    def __init__(self, cb):
        self.cb = cb

    def execute(self):
        self.cb.execute()


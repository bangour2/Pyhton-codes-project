__author__ = 'mohammad'

class CodeBlock():

    def __init__(self):
        self.stmts = []

    def execute(self):
        for stmt in self.stmts:
            stmt.execute()

    def insert (self, stmt):
        self.stmts.append(stmt)

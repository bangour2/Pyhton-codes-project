__author__ = 'mohammad'

from Tokens import Token
from TokenTypes import TokenType
from LexicalExceptions import LexicalException

class LexicalAnalyzer():

    def __init__(self, file_name):
        self.token_list = []
        line_number = 1
        f = open (file_name, 'r')
        for line in f:
            self.process_line (line, line_number)
            line_number += 1
        f.close()
        self.token_list.append(Token (line_number, 1, 'EOS', TokenType.EOS_TOK))

    def process_line (self, line, line_number):
        column_number = 0
        column_number = self.skip_white_space (line, column_number)
        while column_number < len(line):
            lexeme = self.get_lexeme (line, column_number)
            tok_type = self.determine_token_type (lexeme, line_number, column_number)
            tok = Token (line_number, column_number + 1, lexeme, tok_type)
            self.token_list.append(tok)
            column_number += len(lexeme)
            column_number = self.skip_white_space (line, column_number)

    def determine_token_type (self, lexeme, line_number, column_number):
        if lexeme.isalpha(): #is a string
            if len (lexeme) == 1: #lenght of lexeme ==1
                tok_type = TokenType.ID_TOK
            elif lexeme == "IF":
                tok_type = TokenType.IF_TOK
            elif lexeme == "UNTIL":
                tok_type = TokenType.UNTIL_TOK
            elif lexeme == "REPEAT":
                tok_type = TokenType.REPEAT_TOK
            elif lexeme == "THEN":
                tok_type = TokenType.THEN_TOK
            elif lexeme == "ELSE":
                tok_type = TokenType. ELSE_TOK
            elif lexeme == "END":
                tok_type = TokenType.END_TOK
            elif lexeme == "WriteInt":
                tok_type = TokenType.WriteInt_TOK
            elif lexeme == "BEGIN":
                tok_type = TokenType.BEGIN_TOK
            elif lexeme == "WHILE":
                tok_type = TokenType.WHILE_TOK
            elif lexeme == "DO":
                tok_type = TokenType.DO_TOK
            elif lexeme == "MODULE":
                tok_type = TokenType.MODULE_TOK
                
            else:
                raise LexicalException ("invalid lexeme at row " + str(line_number) + " and column" +
                                        str(column_number + 1))
        elif lexeme.isdigit():
            tok_type = TokenType.LIT_INT
        elif lexeme == ":=":
            tok_type = TokenType.ASSIGN_OP
        elif lexeme == "+":
            tok_type = TokenType.ADD_TOK
        elif lexeme == "-":
            tok_type = TokenType.SUB_TOK
        elif lexeme == "*":
            tok_type = TokenType.MUL_TOK
        elif lexeme == "/":
            tok_type = TokenType.DIV_TOK
        elif lexeme == "==":
            tok_type = TokenType.EQ_TOK
        elif lexeme == "/=":
            tok_type = TokenType.NE_TOK
        elif lexeme == "<":
            tok_type = TokenType.LT_TOK
        elif lexeme == "<=":
            tok_type = TokenType.LE_TOK
        elif lexeme == ">":
            tok_type = TokenType.GT_TOK
        elif lexeme == ">=":
            tok_type = TokenType.GE_TOK
        elif lexeme == "(":
            tok_type = TokenType.LEFT_PAREN_
        elif lexeme == ")":
            tok_type = TokenType.RIGHT_PAREN_
        elif lexeme == ";":
            tok_type = TokenType.SEMICOLON_TOK

        elif lexeme == ".":
            tok_type = TokenType.PERIOD_TOK
        else:
            raise LexicalException ("invalid lexeme at row " + str(line_number) + " and column" +
                                        str(column_number + 1))
        return tok_type

    def is_white_space (self, ch):
        return ch == ' ' or ch == '\n' or ch == '\t'

    def skip_white_space (self, line, index):
        while index < len(line) and self.is_white_space(line[index]):
            index += 1
        return index

    def get_lexeme (self, line, index):
        i = index
        while i < len(line) and not self.is_white_space (line[i]):
            i += 1
        return line[index: i]

    def get_next_token (self):
        if self.token_list.__len__() == 0:
            raise LexicalException ("no more tokens")
        return self.token_list.pop(0)

    def get_lookahead_token (self):
        if self.token_list.__len__() == 0:
            raise LexicalException ("no more tokens")
        return self.token_list[0]


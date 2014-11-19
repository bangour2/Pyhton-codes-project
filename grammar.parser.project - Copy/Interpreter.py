__author__ = 'mohammad'


from Parsers import Parser
from ParserExceptions import ParserException
from LexicalExceptions import LexicalException

if __name__ == '__main__':
    try:
        p = Parser ('test4.rb')
        prog = p.parse()
        prog.execute()
    except ParserException as e:
        print (e.message)
    except LexicalException as e:
        print (e.message)
    except Exception as e:
        print ("unknown error occurred - terminating")

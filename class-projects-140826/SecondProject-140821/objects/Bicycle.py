__author__ = 'student'

class Bicycle(object):
    ''' i am a class
    '''

    width = 30  ## this is a  class variable (static)

    def __init__(self, color):
        self.length = 20  # defines an instance field named length
        self.color = color

    def printSome(self):
        print("length", self.length)
        print("color", self.color)
        print("width", Bicycle.width)
        print("width", self.width)
        print("width", width)

    def setColor(self, newColor):
        self.color = newColor

    def aMethod(self, *params):
        for p in params:
            print(p)

    # allow arbitrary keyword parameters
    def anotherMethod(self, **params):
        for key in params:
            print(key, params[k])

# not in the class definition
x = Bicycle('green')
print(x)
print(x.length)
print(x.color)
x.material = "jello"
print(x.material)
print(Bicycle.width)

width = "something else"

x.printSome()

x.setColor("blue")

x.printSome()


x.setColor(newColor="brown")
x.printSome()



















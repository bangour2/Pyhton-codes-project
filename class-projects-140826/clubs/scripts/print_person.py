
__author__ = 'Ben'

import clubs #folder
import sys

if __name__ == '__main__':
    dataset = clubs.Sample1() # class
    if len(sys.argv) != 2:
        print("provide exactly one argument: a person's id")
        sys.exit(1)
    id = int(sys.argv[1])
    # print("id is {:d}".format(id))
    person = dataset.findPersonById(id)
    if person :
        print(person)
        if person.presidentOf:
            print("  Is president of " + person.presidentOf.name)
        for c in person.memberOf:
            print("  member of " + c.name)
    else:
        print("Person with id {0} is not in the dataset".format(id))


   # print(sys.argv[1] + sys.argv[2])


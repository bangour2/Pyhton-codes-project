__author__ = 'student'

from jinja2 import Environment, FileSystemLoader

# calling this function will create our error page
# The messages parameter is a list of all positional parameters passed to the function
def page(*msgs):

    print("Content-Type: text/html; charset=UTF-8")
    print("")

    # create a loader to get templates
    ldr = FileSystemLoader('templates')
    # initialize an environment
    env = Environment(loader=ldr)
    # get a template, pre-compilation
    tmplt = env.get_template("error_page.html")
    # render to a string
    rndrd = tmplt.render(messages=msgs)
    # send as the response
    print(rndrd)



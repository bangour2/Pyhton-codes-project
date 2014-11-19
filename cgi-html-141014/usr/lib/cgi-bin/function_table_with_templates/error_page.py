__author__ = 'student'

# calling this function will create our error page
# The messages parameter is a list of all positional parameters passed to the function
def page(*messages):


    page_top = """
    <!DOCTYPE html>
    <html>
    <head lang="en">
        <meta charset="UTF-8">
        <title>Error</title>
        <link href="/style1.css" rel="stylesheet" type="text/css"/>
    </head>
    <body>
        <h1>Data Entry Error</h1>
    """

    page_bottom = """
    </body>
    </html>
    """
    print(page_top)

    print("<ul>")
    for msg in messages:
        print("<li class='error'>{}</li>".format(msg))

    print("</ul>")

    print("<h2>Use the back button and reeneter the data correctly</h2>")

    print(page_bottom)
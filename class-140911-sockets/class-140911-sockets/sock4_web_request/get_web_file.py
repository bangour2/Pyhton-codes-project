__author__ = 'Ben Setzer'

from sock1_reader_writer import reader_writer
from socket import socket

sock = socket()
sock.connect(("cs.kennesaw.edu",80))

request = """GET /~bsetzer/index.html HTTP/1.1
Host: cs.kennesaw.edu

"""

rw = reader_writer(sock)
rw.write(request)
rw.close_write()

c = rw.read()
while len(c) > 0:
    print(c, end="")
    c = rw.read()


sock.close()
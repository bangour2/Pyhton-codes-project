__author__ = 'student'

import reader_writer
from socket import socket

sock = socket()

sock.connect(('localhost',12345))

print("Connection made")

rw = reader_writer(sock)

data = '5 6 * 7 * 9 * 10 * *'
rw.write(data)
rw.close_write()

print("sending done")

c = rw.read()
while c:
    print(c,end='')
    c = rw.read()

sock.close()
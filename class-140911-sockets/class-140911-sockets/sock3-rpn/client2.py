__author__ = 'student'

from sock1_reader_writer.reader_writer import reader_writer
from socket import socket

sock = socket()

sock.connect(('localhost',12347))

print("Connection made")

rw = reader_writer(sock)



rw.write('1 ')
for i in range(2,40):
    rw.write(' ' + str(i) + ' * ')

rw.close_write()

print("sending done")

c = rw.read()
while c:
    print(c,end='')
    c = rw.read()

sock.close()
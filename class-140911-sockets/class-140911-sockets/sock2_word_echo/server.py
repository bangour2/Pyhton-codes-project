__author__ = 'student'

# the project root directory is in the PYTHON_PATH
# So, we have start there to get to reader_writer
from sock1_reader_writer.reader_writer import reader_writer

from socket import socket


# create and configure a listener (server) socket
listener_socket = socket()
listener_socket.bind(('',12345))   #  host:  listen on any ip address
                                    # port: 12345
listener_socket.listen(5)

while True:
    (conn, address) = listener_socket.accept()

    rw = reader_writer(conn)

    word = rw.next_word()
    while len(word) > 0:
        #print(word)
        rw.write(word+"\n")
        word = rw.next_word()

    rw.close_write()

    conn.close()


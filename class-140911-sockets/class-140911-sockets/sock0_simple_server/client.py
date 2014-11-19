__author__ = 'Ben Setzer'


from socket import socket

sock = socket()

sock.connect(('localhost',12347))


print("Connection made")



byte_data = "hello There!  Jan Łukasiewicz".encode("utf-16")  # convert string characters to bytes

sock.send(byte_data)



sock.close()

__author__ = 'Ben Setzer'


from socket import socket

listener_socket = socket()

listener_socket.bind(('',12347))   #  host:  listen on any ip address
                                    # port: 12345

listener_socket.listen(5)

print("Now calling accept function")

(sock, address) = listener_socket.accept()
# script is now waiting for a connection

print("Connection made and accepted")

print("socket is " + str(sock))
print("address is " + str(address))


rcvd_data = sock.recv(2048)
print("received", rcvd_data)
rcvd_string = rcvd_data.decode("utf-16")
print("received string", rcvd_string)

sock.close()

listener_socket.close()
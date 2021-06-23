# HREF: https://wiki.python.org/moin/UdpCommunication

import socket

UDP_SERVER_IP_ADDRESS = "127.0.0.1"
UDP_SERVER_PORT = 6789

serverSock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM,
)

serverSock.bind((
    UDP_SERVER_IP_ADDRESS,
    UDP_SERVER_PORT,
))

print("Listening at {}:{}".format(UDP_SERVER_IP_ADDRESS, UDP_SERVER_PORT))

while True:
    data, addr = serverSock.recvfrom(1024)
    print("Message: ", data)

# HREF: https://wiki.python.org/moin/UdpCommunication

import socket

UDP_SERVER_IP_ADDRESS = "127.0.0.1"
UDP_SERVER_PORT = 6789

MESSAGE = b"Hello, World!"

sock = socket.socket(
    socket.AF_INET,
    socket.SOCK_DGRAM,
)

sock.sendto(
    MESSAGE,
    (
        UDP_SERVER_IP_ADDRESS,
        UDP_SERVER_PORT,
    )
)

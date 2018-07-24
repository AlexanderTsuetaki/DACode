#!/usr/bin/env python

import socket
from socket import *


def send_data(msg):

    """TCP_IP = '207.235.52.106'
    TCP_PORT = 13000
    BUFFER_SIZE = 1024

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((TCP_IP, TCP_PORT))
    data = None
    while not data:
        s.send(msg)
        data = s.recv(BUFFER_SIZE)
    s.close()"""

    import os
    host = "10.18.13.19" # set to IP address of target computer
    port = 13000
    addr = (host, port)
    UDPSock = socket(AF_INET, SOCK_DGRAM)
    data = msg
    UDPSock.sendto(data, addr)
    UDPSock.close()
    os._exit(0)

#!/usr/bin/env python

import socket

from CONST_DEFINE import SRV_ADDR, SRV_PORT, BUFFER_SIZE
MESSAGE = "Hello, World!"

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.connect((SRV_ADDR, SRV_PORT))
s.connect(('192.168.1.100', 10086))
s.send(b'Hello, World')
data = s.recv(BUFFER_SIZE)
s.close()

print(data)

#!/usr/bin/env python3

import socket
import sys
import operator

HOST = '127.0.0.1'
PORT = 65432
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
inp = [0,0,0]

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open server
s.bind(('', PORT))

for x in range(3):
    # Receive request
    message, addr = s.recvfrom(1024)
    if not message:
        break
    inp[x] = message.decode()

result = str(ops[inp[0]](int(inp[1]), int(inp[2]))).encode()
s.sendto(result, addr)

s.close()                


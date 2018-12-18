#!/usr/bin/env python3

# TO DO: handle keyerror exception

import socket
import sys
import operator
import random

HOST = '127.0.0.1'
PORT = 65432
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
inp = [0,-1,-1]
status = 200

# Create socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Open server
s.bind(('', PORT))

for x in range(3):
    # Receive request
    message, addr = s.recvfrom(1024)
    if not message:
        break
    
    # Random drop
    drop = random.randint(0, 1)
    if drop == 1:
        inp[x] = message.decode()
 

if int(inp[1]) < 0 or int(inp[2]) < 0:
    status = 300
    result = -1
else:
    try:
        result = str(ops[inp[0]](int(inp[1]), int(inp[2]))).encode()
    except KeyError:
        status = 300
        result = -1
    
s.sendto(str(status).encode(), addr)
s.sendto(str(result).encode(), addr)

s.close()                


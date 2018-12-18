#!/usr/bin/env python3 

import socket
import sys
import time

HOST = '127.0.0.1'
PORT = 65432

OC = (input('Enter an operator (+, -, *, /): ')).encode()
first_num = (input('Enter first number: ')).encode()
second_num = (input('Enter second number: ')).encode()

# Creates socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Sends data stream
s.sendto(OC, (HOST, PORT))
s.sendto(first_num, (HOST, PORT))
s.sendto(second_num, (HOST, PORT))

# Receives status code, result

d = 0.1
while d < 2:
    status, addr = s.recvfrom(1024)
    result, addr = s.recvfrom(1024)

    # Timer
    time.sleep(d)
    if status:
        # Successful 
        print('Status: ' + status.decode())
        print('Result: ' + result.decode())
        break

    # Timer expires
    d = 2*d

if d >= 2:
    raise Exception("Dropped packet!")

s.close()
    

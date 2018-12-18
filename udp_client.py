#!/usr/bin/env python3 

import socket
import sys

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

message, addr = s.recvfrom(1024)
print(message.decode())

s.close()
    




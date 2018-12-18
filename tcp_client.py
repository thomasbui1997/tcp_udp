#!/usr/bin/env python3 

import socket

HOST = '127.0.0.1'
PORT = 65432

OC = (input('Enter an operator (+, -, *, /): ') + ' ').encode()
first_num = (input('Enter first number: ') + ' ').encode()
second_num = (input('Enter second number: ') + ' ').encode()

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))

    # Sends data stream
    s.sendall(OC)
    s.sendall(first_num)
    s.sendall(second_num)

    # Receives status code, result

    status = s.recv(1024).decode()
    result = s.recv(1024).decode()

    if not status or int(status) != 200:
        print('Error: Invalid request')
    print('Status: ' + status)
    print('Result: ' + result)




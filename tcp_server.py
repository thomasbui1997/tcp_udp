#!/usr/bin/env python3

import socket
import operator

HOST = '127.0.0.1'
PORT = 65432
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
inp = [0,0,0]

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # Open server
    s.bind((HOST, PORT))

    # Listen to socket
    s.listen()
    conn, addr = s.accept()
    status = 200
    
    with conn:
        print('Connected by', addr)
        while True:
            # Receive request
            data = conn.recv(1024)
            if not data:
                break

            # Separates data received from stream
            res_arr = data.decode().split()
            # Checks for invalid data
        
            try:
                result = ops[res_arr[0]](int(res_arr[1]), int(res_arr[2]))
            except (KeyError, ValueError):
                status = 300
                result = -1

            # Sends status code, result
            conn.sendall(str(status).encode())
            conn.sendall(str(result).encode())
            


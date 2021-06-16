import sys

import socket

s = socket.socket()

HOST, PORT = "15.206.88.194", 5001
s.connect((HOST,  PORT))


while True :

	to_send = sys.stdin.read(1) 
	print(f" sending ... { to_send }")
	s.send(to_send.encode())
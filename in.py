import socket
import sys
s = socket.socket()
s.connect(("15.206.88.194", 5000))
while True:
	inp = s.recv(1024).decode()
	if "quit" in inp:
		print("exit")
		s.close()
		break
	sys.stdout.write(inp)
	sys.stdout.flush()


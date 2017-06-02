import socket
import sys

#creating a socket
def socketCreate():
    try :
        global host
        global port
        global s
        host = ""
        port = 999
        s = socket.socket()
    except socket.error as msg :
        print("socket error : " + str(msg))

# bind the data to the socket
def socketBind():
    try :
        global host
        global port
        global s
        print("binding the socket with the port number : " + str(port))
        s.bind((host, port))
        s.listen(5)
    except socket.error as msg:
        print("socket error : " + str(msg) +"\n"+ "Retrying...")
        socketBind()

#Establish a Connection
def socketAccept():
    conn, adress = s.accept()
    print("Connection has been established | IP : "+ adress[0] +" | port number :" + str(adress[1]) )
    sendCommands(conn)
    conn.close()

def sendCommands(conn):
    while(1):
        try:
            cmd = input()
            if cmd == "quit":
                conn.close()
                s.close()
                sys.exit()
            if len(str(cmd)) > 0:
                conn.send(str.encode(cmd))
                clientResponse = str(conn.recv(1024), "utf-8")
                print(clientResponse)
                break
        except:
            print("invalid command \n")

def main():
    socketCreate()
    socketBind()
    socketAccept()

main()



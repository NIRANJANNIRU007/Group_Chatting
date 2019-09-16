import socket
from time import ctime
import threading

sADDR = ('127.0.0.1', 53437)
buff = 1024

cliSock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliSock.connect(sADDR)

def receive():
    rMessage=''
    while not rMessage=='bye':
        rMessage = cliSock.recv(buff)
        if not rMessage:
            print "Ending connection"
            break
        print "[{0}]: {1}".format(ctime(), rMessage)
    cliSock.close()

def send():
    sMessage=''
    while not sMessage=='bye':
        sMessage = raw_input(">>")
        cliSock.send(sMessage)
    cliSock.close()

t1 = threading.Thread(target=send, name=1)
t2 = threading.Thread(target=receive, name=2)

t1.start()
t2.start()

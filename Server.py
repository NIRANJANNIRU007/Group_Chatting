import socket
import threading
from time import ctime,sleep

ls=dict()
def receive(cliSock,addr):
    rMessage=''
    while not rMessage=='bye':
        rMessage = cliSock.recv(1024)
        if not rMessage:
            print "Ending connection"
            break
        print "{2}: [{0}]: {1}".format(ctime(), rMessage,addr)
        shareclientmsg(rMessage,addr)
    cliSock.close()
def shareclientmsg(msg,addr):
    for addre,cliSock in ls.items():
        if not addre ==  addr:
            cliSock.send(msg)
    

def send(s):
    while True:
        sMessage = raw_input(">>")
        for cliSock in ls.values():
            cliSock.send(sMessage)
        if sMessage == 'bye':
            #s.close()
            break
        


def listenSock(s):
    t=threading.Thread(target=send,args=(s,))
    t.start()
    while s:
        s.listen(5)
        c, addr = s.accept()
        ls[addr]=c
        print('Got connection from', addr)
        t2=threading.Thread(target=receive,args=(c,addr,))
        t2.start()
        #sleep(10)
        

def main(): 
    s = socket.socket()		 
    print("Socket successfully created")

    port = 53437				

    s.bind(('127.0.0.1', port))		 
    print("socket binded to %s" %(port)) 
    
    t1=threading.Thread(target=listenSock,args=(s,))
    t1.start()
    
    
    
if __name__ == "__main__":
    main()

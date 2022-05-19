
import sys
import socket

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()

port = 9999

serversocket.bind((host,port))

serversocket.listen(5)

while True:
    clientsocket,addr = serversocket.accept()

    print("链接地址：%s"%str(addr))

    msg = '欢迎光临socket'+"\r\n"
    clientsocket.send(msg.encode('utf-8'))
    clientsocket.close()

    

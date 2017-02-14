#!/usr/bin/python3
import socket

mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySocket.bind((socket.gethostname(),1231))
mySocket.listen(5)

try:
    while True:
        print('Waiting connections')
        (recvSocket,address) = mySocket.accept()
        print('HTTP request received:')
        print(recvSocket.recv(2048))
        recvSocket.send(bytes("HTTP/1.1 404 Not Found\r\n\r\n" +
                        "<!DOCTYPE html><html><head><title> Probando Sockets </title>" +
                        "<body><h1>404 Not Found</h1>" +
                        "</body></html> \r\n","utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()

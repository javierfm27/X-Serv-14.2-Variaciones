#!/usr/bin/python3
import socket

mySocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
mySocket.bind((socket.gethostname(),1232))
mySocket.listen(5)

try:
    while True:
        print('Waiting connections')
        (recvSocket,address) = mySocket.accept()
        print('HTTP request received:')
        print(recvSocket.recv(2048))
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        "<!DOCTYPE html><html><head> <meta http-equiv='REFRESH' content='5'; url='http://www.desarrolloweb.com'> " +
                        "<title> Probando Sockets </title></head>" +
                        "<body><h4>Redireccionando</h4>" +
                        "</body></html> \r\n","utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()

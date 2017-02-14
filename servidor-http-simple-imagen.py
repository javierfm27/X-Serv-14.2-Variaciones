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
        recvSocket.send(bytes("HTTP/1.1 200 OK\r\n\r\n" +
                        "<!DOCTYPE html><html><head><title> Probando Sockets </title>" + 
                        "<body><h1>Imagen Random</h1>" +
                        "<img src='http://www.miataturbo.net/attachments/insert-bs-here-4/78009d1370019848-random-pictures-thread-only-rule-keep-sfw-1682345-slide-slide-1-biz-stone-explains-how-he-turned-91-random-photos-into-movie-jpg'></img>" +
                        "</body></html> \r\n","utf-8"))
        recvSocket.close()
except KeyboardInterrupt:
    print ("Closing binded socket")
    mySocket.close()

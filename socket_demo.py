import socket

HOST = '192.168.137.137'
PORT = 80
BUFSIZ =1024
ADDR = (HOST,PORT)
 
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)
while True:
     data1 = input('>')
     #data = str(data)
     if not data1:
        continue
     client.send(data1.encode('utf-8'))
     data1 = client.recv(BUFSIZ)
     if not data1:
        break
     print(data1.decode('utf-8'))
client.close()
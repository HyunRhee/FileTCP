#!/usr/bin/python3
import socket

host = ''
port = 12898
buff_size = 128
backlog = 5

conn_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
conn_sock.bind(server_address)

conn_sock.listen(backlog)

while True:
    print("waiting for request...")
    data, address = conn_sock.accept()
    print("echo request from {} port {}".format(address[0], address[1]))
    message = data.recv(buff_size)
    accessMode = "r"
    try:
        if message:
            print("received message : {} \n".format(message.decode()))
            myFile = open(message, accessMode)
            dataFile = myFile.read()
            print(dataFile)
            data.sendall(dataFile.encode())
            myFile.close()

    except FileNotFoundError:
        print("파일명을 찾을 수 없습니다.")

    data.close()
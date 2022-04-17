import socket


host = '127.0.0.1'
port = 12898
buff_size = 128

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = (host, port)
print("connecting to {} port {}".format(server_address[0], server_address[1]))
sock.connect(server_address)

message = input("Eenter filename : ")
message = bytes(message, encoding = 'utf-8')


try :
    sock.sendall(message)
    data = sock.recv(buff_size)
    data = data.decode()

    if data :
        print("Received from server : \n{}".format(data))
        accessMode = 'w'
        filename = message
        myFile = open(filename, accessMode)
        myFile.write(data)
        print("\n")
        print("파일이 성공적으로 저장되었습니다.")
    else:
        print("\n")
        print("서버에서 파일명을 찾을 수 없습니다.")

except Exception as e:
     print("Exception : {}".format(str(e)))

sock.close()
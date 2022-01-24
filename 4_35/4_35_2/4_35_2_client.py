from socket import *
HOST = 'localhost'
PORT = 3333

tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.connect((HOST, PORT))

while True:
    msg = input('Send data to server:')
    if msg == 'stop':
        break
    tcp_socket.send(msg.encode())
    msg_from_server = tcp_socket.recv(1024)
    print(msg_from_server.decode())

tcp_socket.close()

from socket import *
from threading import Thread

HOST = 'localhost'
PORT = 3333


class ClientThread(Thread):

    def __init__(self, ip, port, client_socket):
        super().__init__()
        self.ip = ip
        self.port = port
        self.cl_sock = client_socket
        print(f'New thread created for client: {self.ip, self.port}')

    def run(self):
        self.cl_sock.send('Connected to the server'.encode())

        msg = None
        while msg != 'disconnect':
            msg = self.cl_sock.recv(1024)
            print(f'Client {self.ip, self.port} says: {msg.decode()}')
            cl_sock.send('Message received'.encode())

        print(f'Client {self.ip, self.port} disconnected')


tcp_socket = socket(AF_INET, SOCK_STREAM)
tcp_socket.bind((HOST, PORT))
tcp_socket.listen(5)

while True:
    (cl_sock, (ip, port)) = tcp_socket.accept()
    cl_thread = ClientThread(ip, port, cl_sock)
    cl_thread.start()

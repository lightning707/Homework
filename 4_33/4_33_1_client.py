from socket import *


while True:
    try:
        msg = input("msg: ")

        sock = socket(AF_INET, SOCK_DGRAM)

        if msg == 'quit':
            sock.close()
            break

        sock.sendto(msg.encode(), ('localhost', 4000))

        server_resp = sock.recvfrom(100)
        print(f'Message from server: {server_resp}')
    finally:
        sock.close()

from socket import *

msg_from_server = "UDP connected"

try:
    sock = socket(AF_INET, SOCK_DGRAM)
    sock.bind(('localhost', 4000))
    while True:
        client_msg, client_addr = sock.recvfrom(1000)

        print(f"Recieved message: {client_msg} from {client_addr}")

        sock.sendto(msg_from_server.encode(), client_addr)
finally:
    sock.close()

import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 3003

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
    sock.connect((UDP_IP, UDP_PORT))
    sock.sendall(b'Any words')
    data = sock.recv(1024)

print(f'Recieved: {repr(data)}')


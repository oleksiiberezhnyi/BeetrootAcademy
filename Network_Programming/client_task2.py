import socket
import pickle

UDP_IP = '127.0.0.1'
UDP_PORT = 3003

text = 'Beetroot Academy. Homework 31. Task 2.'
key = 4
message = pickle.dumps((text, key))


with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
    client.connect((UDP_IP, UDP_PORT))
    client.sendall(message)
    data = client.recv(1024)

print(f'Encrypted text: {pickle.loads(data)}')


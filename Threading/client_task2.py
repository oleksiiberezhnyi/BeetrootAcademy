import socket

IP = '127.0.0.1'
PORT = 3003


while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.connect((IP, PORT))
        sock.sendall(input("input:").encode())
        data = sock.recv(2048)
        print(f'Recieved: {data.decode()}')

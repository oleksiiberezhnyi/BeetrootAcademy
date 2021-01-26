import socket
import threading


class ClientConnectionThread(threading.Thread):

    def __init__(self, ip, port, socket):
        super().__init__()
        self._ip = ip
        self._port = port
        self._socket = socket


    def run(self):
        print(f'Connection from: {self._ip}:{str(self._port)}')
        self._socket.send(f'Connected to server'.encode())
        data = self._socket.recv(2048)
        while len(data):
            data = self._socket.recv(2048)
            self._socket.send(f'Send: {data}'.encode())
        # print(f'Client connection at {self._ip}:{str(self._port)} disconnected')

IP = '127.0.0.1'
PORT = 3003

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((IP, PORT))
server.listen(4)

# print(f'TCP target IP: {IP}')
# print(f'TCP target port: {PORT}')

while True:
    print('Waiting ...')
    (sock, (ip, port)) = server.accept()
    ClientConnectionThread(ip, port, sock).start()
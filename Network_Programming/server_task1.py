import socket

UDP_IP = '127.0.0.1'
UDP_PORT = 3003

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((UDP_IP, UDP_PORT))

print(f'UDP target IP: {UDP_IP}')
print(f'UDP target port: {UDP_PORT}')

while True:
    print('Waiting ...')
    message, address = server.recvfrom(1024)
    if message:
        message = message.upper()
        print(f'message: {message}')
        server.sendto(message, address)
    else:
        print(f'no data from: {address}')
        server.close()
        break

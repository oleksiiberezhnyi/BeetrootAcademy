import socket
import pickle


def encrypt(text, s):
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            result += chr((ord(char) + s - 65) % 26 + 65)
        else:
            result += chr((ord(char) + s - 97) % 26 + 97)
    return result


UDP_IP = '127.0.0.1'
UDP_PORT = 3003

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((UDP_IP, UDP_PORT))

print(f'UDP target IP: {UDP_IP}')
print(f'UDP target port: {UDP_PORT}')

while True:
    print('Press Control+C to exit\nWaiting...')
    message, address = server.recvfrom(1024)
    if message:
        message = pickle.loads(message)
        message_encrypt = encrypt(message[0], message[1])
        print(f'message: {message[0]}, key: {message[1]}\n'
              f'encrypt message: {message_encrypt}')
        message_encrypt = pickle.dumps(message_encrypt)
        server.sendto(message_encrypt, address)
    else:
        print(f'no data from: {address}')
        server.close()
        break



import socket
from server_task2 import Style

IP = '127.0.0.1'
PORT = 3003


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    try:
        client.connect((IP, PORT))
        while True:
            client.send(input("input:").encode())
            data = client.recv(2048)
            print(f'Recieved: {data.decode()}')
    except KeyboardInterrupt:
        print(f'{Style.YELLOW}'
              f'\nBye...'
              f'{Style.END}'
              )
    except Exception:
        print(f'{Style.YELLOW}'
              f'\nOops...'
              f'{Style.END}'
              )

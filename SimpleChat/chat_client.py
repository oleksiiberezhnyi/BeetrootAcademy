import socket
import json
import datetime
import threading


class Style:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


IP = '10.10.1.64'
PORT = 9091

print(datetime.datetime.utcnow().strftime('[%Y-%m-%d %H:%M:%S]'))


class Connection(threading.Thread):

    def __init__(self, connection):
        super().__init__()
        self._conn = connection

    def run(self):
        while True:
            data = client.recv(1024)
            if len(data) == 0:
                continue
            data_decode = json.loads(data).decode()
            print(data)
            print(data_decode)
            if 'error' in data_decode:
                print(f'Error: {data_decode["error"]["code"]}')
            else:
                print(
                    f'{datetime.datetime.utcnow().strftime("[%Y-%m-%d %H:%M:%S]")}'
                    f'{data_decode["user_name"]}'
                    f'{data_decode["message"]}')


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
    # try:
    id = 1
    users = []
    user_name = 'Oleksii'
    users.append(user_name)
    client.connect((IP, PORT))
    while True:
        message = input('message: ')
        data_to_all = {'user_name': user_name,
                       'message': message,
                       'recipient': 'Ivan2'
                       }
        client.send(json.dumps(data_to_all).encode())

#     # except KeyboardInterrupt:
#     #     print(f'{Style.YELLOW}'
#     #           f'\nBye...'
#     #           f'{Style.END}'
#     #           )
#     # except Exception:
#     #     print(f'{Style.YELLOW}'
#     #           f'\nOops...'
#     #           f'{Style.END}'
#     #           )

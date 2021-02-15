import requests
import json
import datetime
from random import randrange


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



URL = 'http://127.0.0.1:5000/chat'

name = 'Oleksii'
id = randrange(1000, 9999)

user_name = f'{id}Oleksii'

while True:
    date = datetime.datetime.utcnow().strftime('[%Y-%m-%d %H:%M:%S]')
    message = input(f'{Style.BLUE}'
                    f'{date}{Style.END}: '
                    )
    if message.find('@') >= 0:
        recipient = message[message.find('@') + 1: message.find(':')]
        data_to_all = {'user_name': user_name,
                       'message': message[message.find(':'):],
                       'recipient': recipient
                       }
    else:
        data_to_all = {'user_name': user_name,
                       'message': message
                       }
    try:
        requests.post(URL, json.dumps(data_to_all).encode())
    except:
        print(f'{Style.RED}'
              f'Oops. Server not found'
              f'{Style.END}')



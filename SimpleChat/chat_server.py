import socket
import threading
import logging
import json


logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logging.basicConfig(format="{%(process)d:%(threadName)s} - %(message)s")


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


class ClientConnectionThread(threading.Thread):

    def __init__(self, connect: socket.socket, address: tuple):
        super().__init__()
        self._socket = connect
        self._address = address
        logger.info(f'{Style.BLUE}'
                    f'Connection from'
                    f'{self._address[0]}:'
                    f'{self._address[1]}'
                    f'{Style.END}'
                    )

    def run(self):
        message = self._socket.recv(1024)
        self._socket.send(message)
        while message:
            logger.info(f'{Style.CYAN}'
                        f'{self._address[0]}:'
                        f'{self._address[1]}-'
                        f'{message.decode()}'
                        f'{Style.END}'
                        )
            message = self._socket.recv(1024)
            self._socket.send(f'send from server {message}'.encode())
        else:
            logger.info(f'{Style.RED}'
                        f'Connection from '
                        f'{self._address[0]}:'
                        f'{self._address[1]} '
                        f'closed'
                        f'{Style.END}'
                        )


IP = '127.0.0.1'
PORT = 3003


with socket.socket() as server:
    try:
        server.bind((IP, PORT))
        server.listen(4)
        while True:
            connection, address = server.accept()
            ClientConnectionThread(connection, address).start()
    except KeyboardInterrupt:
        print(f'{Style.YELLOW}'
              f'\nBye...'
              f'{Style.END}'
              )
        server.close()
    except Exception:
        server.close()
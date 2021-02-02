import socket
import sys
import json
from typing import Tuple, List
from dataclasses import dataclass, field
import threading
import logging

# logger = logging.getLogger(__name__)
# logger.setLevel(logging.DEBUG)
# logging.basicConfig(
#     format="[%(asctime)s] [%(levelname)s] {%(filename)s:%(lineno)d} {%(process)d:%(threadName)s} - %(message)s")


@dataclass(unsafe_hash=False, eq=False)
class Client:
    connection: socket.socket
    addr: Tuple[str, int]
    name: str = field(default='')

    def __eq__(self, other):
        if not isinstance(other, Client):
            return False
        return self.name == other.name


class Error:

    def __init__(self, error_code):
        self._error_code = error_code
        self._error()

    def _error(self):
        error = {'error': {'code': self._error_code}}
        return error


class Message:

    def __init__(self, message, user_name, recipient=None):
        self._message = message
        self._user_name = user_name
        self._recipient = recipient

    def data(self):
        if self._recipient is None:
            data = {'user_name': self._user_name, 'message': self._message}
        else:
            data = {'user_name': self._user_name, 'message': self._message, 'recipient': self._recipient}
        return data

    # @classmethod
    # def raw(cls, data: str):
    #     try:
    #         data = json.loads(data.replace('\'', '"'))
    #     except Exception:
    #         logger.warning(f'Can not parse message: {data}, {type(data)}')
    #         return None
    #     logger.debug(f'Encoded data: {data}')
    #     return cls(
    #         message=data.get('message'),
    #         user_name=data.get('user_name'),
    #         recipient=data.get('recipient')
    #     )


class Chat:

    clients = []

    class ClientProcessor(threading.Thread):
        def __init__(self, client: Client):
            super().__init__()
            self._client = client

        def run(self, *args, **kwargs):
            data = self._client.connection.recv(1024).decode()
            while data:
                # message = json.loads(data.decode())
                if data:
                    if not self._check_name(data):
                        self._client.connection.send(str(Error(403)).encode())
                    else:
                        Chat.send_message(self._client, data)
                else:
                    self._client.connection.send(str(Error(402)).encode())
                data = self._client.connection.recv(1024).decode()
            else:
                print(f'{self._client.addr}Користувач: {self._client.addr[0]}:{self._client.addr[1]} вийшов з чату')

        def _check_name(self, message):
            if not self._client.name:
                self._client.name = message._user_name
            else:
                for client in Chat.clients:
                    if client.name == self._client.name:
                        return False
            return True

    def __init__(self, ip: str, port: int):
        self._address = ip
        self._port = port

    def start(self):
        with socket.socket() as server:
            try:
                server.bind((self._address, self._port))
                server.listen(2)
                while True:
                    connection, address = server.accept()
                    client = Client(connection, address)
                    Chat.clients.append(client)
                    self.process_client(client)
            except KeyboardInterrupt:
                print(f'Прощавайте, чат зупинено.')
                server.close()
            except OSError:
                print(f'Ой! Адреса зайнята')
                server.close()
            # except Exception:
            #     print(f'Упс, виникла якась халепа.')
            #     server.close()

    def process_client(self, client: Client):
        Chat.ClientProcessor(client).start()

    @classmethod
    def get_recipient(cls, recipient: str):
        recipients = [client for client in cls.clients if
                      client.name == recipient]
        if recipients:
            return recipients[0]

    @classmethod
    def send_message(cls, sender: Client, message: Message):
        logger.info(f'Chat.send_message {message}, sender {sender}')
        if message._recipient:
            recipient: Client = cls.get_recipient(message._recipient)
            if recipient:
                recipient.connection.send(message._message.encode())
            else:
                sender.connection.send(str(Error(401).error()).encode())
        else:
            for client in cls.clients:
                if client == sender:
                    continue
                client.connection.send(str(message.data()).encode())


if __name__ == '__main__':
    chat = Chat('127.0.0.1', 3003)
    chat.start()

import asyncio


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


IP = '127.0.0.1'
PORT = 3003


async def server(reader, writer):
    data = await reader.read(1024)
    print(f'{Style.CYAN}'
          f'Incoming message: {data.decode()}'
          f'{Style.END}'
          )
    writer.write(data)


if __name__ == '__main__':

    loop = asyncio.get_event_loop()
    start_server = asyncio.start_server(server, IP, PORT, loop=loop)
    run_server = loop.run_until_complete(start_server)

    print(f'{Style.GREEN}'
          f'Server start on '
          f'{Style.END}'
          f'{Style.PURPLE}'
          f'{run_server.sockets[0].getsockname()[0]}:'
          f'{run_server.sockets[0].getsockname()[1]}'
          f'{Style.END}')
    try:
        loop.run_forever()
    except KeyboardInterrupt:
        print(f'{Style.YELLOW}'
              f'\nBye...'
              f'{Style.END}'
              )

    run_server.close()
    loop.close()

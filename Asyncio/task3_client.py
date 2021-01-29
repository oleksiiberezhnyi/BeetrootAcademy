import asyncio
from task3_server import Style

IP = '127.0.0.1'
PORT = 3003


async def client(loop):
    reader, writer = await asyncio.open_connection(IP, PORT, loop=loop)
    message = input('Input message: ')
    writer.write(message.encode())
    data = await reader.read(1024)
    print(f'Recieved: {data.decode()}')


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    try:
        while True:
            loop.run_until_complete(client(loop))
    except KeyboardInterrupt:
        print(f'{Style.YELLOW}'
              f'\nBye...'
              f'{Style.END}'
              )
        loop.close()
    except Exception:
        print(f'{Style.YELLOW}'
              f'\nOops...'
              f'{Style.END}'
              )
        loop.close()

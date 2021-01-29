import json
import os
import asyncio
import aiohttp
import aiofiles


URL = 'https://api.pushshift.io/reddit/comment/search'
FILE = 'comments.json'

author_list = ['SweetReptile',
               'toofarbyfar',
               'ImAnonymous135',
               'crescentcactus',
               'AdelineKraxx',
               'bradg2415'
               ]


loop = asyncio.get_event_loop()
connector = aiohttp.TCPConnector(ssl=False, loop=loop)
session = aiohttp.ClientSession(loop=loop, connector=connector)

async def main():
    for author in author_list:
        params = {'size': 5, 'author': author, 'fields': ('author', 'body', 'created_utc')}
        async with session.get(URL, params=params) as response:
            assert response.ok is True
            data = await response.text()
            async with aiofiles.open(FILE, 'a') as file:
                await file.write(data)
                # json.dump(json.loads(data), file, indent=4)
                await file.write(',\n')

    with open(FILE, 'rb+') as file:
        file.seek(-2, os.SEEK_END)
        file.truncate()


if __name__ == '__main__':
    loop.run_until_complete(main())
    loop.close()
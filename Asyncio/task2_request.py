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


async def proceed_author(author):
    async with aiohttp.TCPConnector(ssl=False, loop=loop) as connector:
        params = {'size': 5, 'author': author,
                  'fields': ('author', 'body', 'created_utc')}
        async with aiohttp.ClientSession(loop=loop, connector=connector).get(
                URL, params=params) as response:
            data = await response.text()
            async with aiofiles.open(FILE, 'a') as file:
                await file.write(data)
                await file.write(',\n')


async def main():
    args = [proceed_author(author) for author in author_list]
    await asyncio.gather(*args, loop=loop)


if __name__ == '__main__':
    loop.run_until_complete(main())
    loop.close()

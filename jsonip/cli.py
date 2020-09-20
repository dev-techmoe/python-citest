from aiohttp import ClientSession
import asyncio
from . import version

async def get_ip():
    async with ClientSession(trust_env=True) as sess:
        async with sess.get('https://jsonip.com/') as resp:
            return await resp.json()

def run():
    print('JSONIP Version ' + version.VERSION)
    print(asyncio.run(get_ip()))

if __name__ == '__main__':
    run()
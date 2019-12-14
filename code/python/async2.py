import asyncio
from aiohttp import ClientSession
import time


async def fetch(url, session):
    async with session.get(url) as response:
        return await response.text()


async def fetch_all():
    url = "http://server:8000/"
    tasks = []

    async with ClientSession() as session:
        for _ in range(10):
            task = asyncio.ensure_future(fetch(url, session))
            tasks.append(task)

        return await asyncio.gather(*tasks)


start = time.time()

loop = asyncio.get_event_loop()
responses = loop.run_until_complete(fetch_all())

for response in responses:
    print(response)

print('Time waiting:', time.time() - start, 'secs')

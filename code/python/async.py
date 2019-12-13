import asyncio
from aiohttp import ClientSession
import time

async def fetch(url, session):
    async with session.get(url) as response:
        return await response.read()

async def run(request_count):
    url = "http://server:8000/"
    tasks = []

    async with ClientSession() as session:
        for _ in range(request_count):
            task = asyncio.ensure_future(fetch(url.format(), session))
            tasks.append(task)

        return await asyncio.gather(*tasks)

start = time.time()

loop = asyncio.get_event_loop()
future = asyncio.ensure_future(run(10))
responses = loop.run_until_complete(future)

for response in responses:
    print(response)

print('Time waiting:', time.time() - start, 'secs')

import requests
import asyncio
import time


async def fetch(url):
    response = requests.get(url)
    return response.text


async def fetch_all():
    tasks = []
    for _ in range(1, 10):
        task = asyncio.ensure_future(fetch('http://server:8000'))
        tasks.append(task)
    return await asyncio.gather(*tasks)

start = time.time()

loop = asyncio.get_event_loop()
responses = loop.run_until_complete(fetch_all())

for response in responses:
    print(response)

print('Time waiting:', time.time() - start, 'secs')

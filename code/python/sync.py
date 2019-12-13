import requests
import time

start = time.time()

for _ in range(1, 10):
    response = requests.get('http://server:8000')
    print(response.text)

print('Time waiting:', time.time() - start, 'secs')

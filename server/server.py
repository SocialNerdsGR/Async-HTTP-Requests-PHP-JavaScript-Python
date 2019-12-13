from sanic import Sanic
from sanic.response import json
import random
import time

app = Sanic()

def get_response():
    responses = [
        'Hello SocialNerds!',
        'This is a typical response.',
        'This is not a typical response.',
        'I have no more ideas.',
        'Hello World I guess...'
    ]
    return random.choice(responses)

@app.route('/')
async def test(request):
    time.sleep(0.2)
    return json({'message': get_response()})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, workers=10)

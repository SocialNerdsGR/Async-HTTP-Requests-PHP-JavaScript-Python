# Asynchronous HTTP request in JavaScript, PHP & Python

We explore the asynchronous HTTP request in 3 different programming languages.

# Check the full explanation video (GR)
[![Πώς Πρέπει να Κάνεις HTTP Request, Live
](https://img.youtube.com/vi/UHl7-BrOOoY/0.jpg)](https://www.youtube.com/watch?v=UHl7-BrOOoY)

# Installation
Requirements
- You need to have [Docker](https://docs.docker.com/engine/installation/) and [Docker Compose](https://docs.docker.com/compose/install/) installed

# Run

## Initial setup
Run in root folder,
~~~~
docker-compose build && docker-compose up -d
~~~~

Check your browser on,
~~~~
http://localhost:8000
~~~~

You should see something like this (or some other random message),
~~~~
{"message":"This is a typical response."}
~~~~

## Requests with PHP
Connect to PHP container,
~~~~
docker exec -it app_php bash
~~~~

Install dependencies,
~~~~
composer install
~~~~

Run synchronous requests,
~~~~
php sync.php
~~~~

You should see something like this,
~~~~
{"message":"Hello SocialNerds!"}
{"message":"This is a typical response."}
{"message":"This is a typical response."}
{"message":"This is not a typical response."}
{"message":"Hello World I guess..."}
{"message":"Hello World I guess..."}
{"message":"I have no more ideas."}
{"message":"I have no more ideas."}
{"message":"This is a typical response."}
Time waiting: 3.6275119781494 secs
~~~~

Run async requests,
~~~~
php async.php
~~~~

You should see something like this,
~~~~
{"message":"Hello SocialNerds!"}
{"message":"I have no more ideas."}
{"message":"Hello World I guess..."}
{"message":"Hello SocialNerds!"}
{"message":"I have no more ideas."}
{"message":"I have no more ideas."}
{"message":"This is not a typical response."}
{"message":"Hello World I guess..."}
{"message":"This is not a typical response."}
Time waiting: 0.43093204498291 secs
~~~~

Exit the container,
~~~~
exit
~~~~

## Requests with Node
Connect to Node container,
~~~~
docker exec -it app_node bash
~~~~

Install dependencies,
~~~~
npm install
~~~~

Run async requests,
~~~~
node app.js
~~~~

You should see something like this,
~~~~
{ message: 'Hello SocialNerds!' }
{ message: 'Hello SocialNerds!' }
{ message: 'I have no more ideas.' }
{ message: 'I have no more ideas.' }
{ message: 'This is a typical response.' }
{ message: 'This is a typical response.' }
{ message: 'This is a typical response.' }
{ message: 'I have no more ideas.' }
{ message: 'Hello SocialNerds!' }
{ message: 'This is not a typical response.' }
Time waiting: 1.239 secs
~~~~

Exit the container,
~~~~
exit
~~~~

## Requests with Python
Connect to Python container,
~~~~
docker exec -it app_python bash
~~~~

Run sync requests,
~~~~
python3 sync.py
~~~~

You should see something like this,
~~~~
{"message":"Hello World I guess..."}
{"message":"Hello World I guess..."}
{"message":"I have no more ideas."}
{"message":"Hello World I guess..."}
{"message":"This is a typical response."}
{"message":"Hello World I guess..."}
{"message":"This is not a typical response."}
{"message":"Hello World I guess..."}
{"message":"Hello World I guess..."}
Time waiting: 3.6628832817077637 secs
~~~~

Run async requests,
~~~~
python3 async2.py
~~~~

You should see something like this,
~~~~
{"message":"Hello SocialNerds!"}
{"message":"I have no more ideas."}
{"message":"This is a typical response."}
{"message":"I have no more ideas."}
{"message":"I have no more ideas."}
{"message":"Hello World I guess..."}
{"message":"Hello World I guess..."}
{"message":"I have no more ideas."}
{"message":"This is a typical response."}
{"message":"This is a typical response."}
Time waiting: 0.9198892116546631 secs
~~~~

Exit the container,
~~~~
exit
~~~~

Shutdown the containers,
~~~~
docker-compose down
~~~~

# By SocialNerds
* [SocialNerds.gr](https://www.socialnerds.gr/)
* [YouTube](https://www.youtube.com/SocialNerdsGR)
* [Facebook](https://www.facebook.com/SocialNerdsGR)
* [Twitter](https://twitter.com/socialnerdsgr)

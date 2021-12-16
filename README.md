# popHighLow

Another Higher or Lower style game, this time you rate the popularity of your facebook friends. Written in python and js.

### Attention! To run this, server needs to have a redis instance on port 6379.

This can for example be achived with docker:

`$ docker run --name some-redis -d -p 6379:6379 redis`

With a valid redis instance, and having installed the flask and redis python packages, running game.py should serve the game on localhost port 5000.

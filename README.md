# popHighLow

Another Higher or Lower style game, this time you rate the popularity of your facebook friends. Written in python and js.

### Attention! To run this, server needs to have a redis instance on port 6379.

This can for example be achived with docker:

`$ docker run --name some-redis -d -p 6379:6379 redis`

With a valid redis instance, and having installed the flask and redis python packages, running game.py should serve the game on localhost port 5000.

## CSV fail

Programm küsib alguses csv faili su facebooki sõpradest.

Kasutame formaati profiiliURL | pildiThumbnailURL | nimi | ühisteSõpradeArv

Hetkel kasutasime chromei laiendid "Instant Data Scraper" lehel "facebook.com/user/friends", aga tulevikus tahaks teha seda kuidagi automaatsemaks.
Kui kasutad sama asja, siis rohkemate inimeste info saamikseks peab enne scrapeimist alla kerima.

### Firefoxiga ei tööta pildid

Oleme probleemis teadlikud, aga ei tea miks või kuidas parandada. Millegipärast ei saa firefox hakkama facebookist saadud urlide fetchimisega. Hetkel peab lihtsalt chromei kasutama.

from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from flask_session import Session
from random import choice
from pathlib import Path
from copy import deepcopy
import redis

from CSVParser import csvToDict

def randomSelect(viimaneNimi):
   if viimaneNimi == "start":
      esimene = choice(list(session['people'].keys()))

      while True:
         nimi = choice(list(session['people'].keys()))
         if nimi != esimene:
            return esimene, nimi

   else:
      while True:
         nimi = choice(list(session['people'].keys()))
         if nimi != viimaneNimi:
            return nimi

app = Flask(__name__)

app.config['SESSION_TYPE'] = 'redis'
app.config['SESSION_PERMANENT'] = False
app.config['SESSION_USE_SIGNER'] = True
app.config['SESSION_REDIS'] = redis.from_url('redis://localhost:6379')
app.secret_key = b'41a2fc1a57d9edde2e44a19616490a330726f984ed7470953da97845c36224fb'
app.config['SESSION_COOKIE_SAMESITE'] = "Strict"
Session(app)

@app.route("/", methods=["GET"])
def index():
   return render_template("index.html")

@app.route("/", methods=["POST"])
def csvFind():
   path = Path(request.get_json('file')['file'])
   if path.is_file():
      session['data'] = csvToDict(path)
      return jsonify({'file': 'olemas'})
   return jsonify({'file': 'pole'})

@app.route("/game", methods=["GET"])
def game():
   session['people'] = deepcopy(session['data'])
   session['maxScore'] = len(session['people'].keys())-1
   session['score'] = 0
   try:
      a = session['topScore']
   except:
      session['topScore'] = 0
   return render_template("game.html")

@app.route("/win", methods=["GET"])
def win():
   return render_template("win.html", score=session.get('score', None), topScore=session.get('topScore', None))

@app.route("/lose", methods=["GET"])
def lose():
   return render_template("lose.html", score=session.get('score', None), maxScore=session['maxScore'], topScore=session.get('topScore', None))

@app.route("/game", methods=["POST"])
def endpoint():
   nimi = str(request.get_json('nimi')['nimi'])

   if nimi == 'start':
      randomFriendStarter, randomFriend = randomSelect(nimi)
      return jsonify({'given': [randomFriendStarter, session['people'].pop(randomFriendStarter)], 'guess': [randomFriend, session['people'][randomFriend]], 'score': session['score'], 'topScore': session['topScore']})
   else:
      session['score'] += 1
      if session['score'] > session['topScore']:
         session['topScore'] = session['score']

      if session['score'] == session['maxScore']:
         return jsonify({'võit': 'jah', 'score': session['score'], 'topScore': session['topScore']})

      randomFriend = randomSelect(nimi)
      return jsonify({'given': [nimi, session['people'].pop(nimi)], 'guess': [randomFriend, session['people'][randomFriend]], 'score': session['score'], 'topScore': session['topScore']})
      


if __name__ == '__main__':
   app.run(debug = True)
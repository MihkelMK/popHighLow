from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from random import choice

from csv_to_list import csvToDict

rawData = csvToDict("hedy.csv")
maxScore = len(rawData.keys())-1

app = Flask(__name__)
app.secret_key = b'41a2fc1a57d9edde2e44a19616490a330726f984ed7470953da97845c36224fb'
app.config['SESSION_COOKIE_SAMESITE'] = "Strict"

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


@app.route("/", methods=["GET"])
def index():
   return render_template("index.html")

@app.route("/game", methods=["GET"])
def game():
   session['people'] = rawData
   session['score'] = 0
   return render_template("game.html")

@app.route("/win", methods=["GET"])
def win():
   return render_template("win.html", score=session.get('score', None))

@app.route("/lose", methods=["GET"])
def lose():
   return render_template("lose.html", score=session.get('score', None), maxScore=maxScore)

@app.route("/game", methods=["POST"])
def endpoint():
   nimi = str(request.get_json('nimi')['nimi'])

   if nimi == 'start':
      randomFriendStarter, randomFriend = randomSelect(nimi)
      return jsonify({'given': [randomFriendStarter, session['people'].pop(randomFriendStarter)], 'guess': [randomFriend, session['people'][randomFriend]], 'score': session['score']})
   else:
      session['score'] += 1
      if session['score'] == maxScore:
         return jsonify({'võit': 'jah', 'score': session['score']})

      randomFriend = randomSelect(nimi)
      return jsonify({'given': [nimi, session['people'].pop(nimi)], 'guess': [randomFriend, session['people'][randomFriend]], 'score': session['score']})
      


if __name__ == '__main__':
   app.run(debug = True)
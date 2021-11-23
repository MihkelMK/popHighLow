from flask import Flask, render_template, jsonify, request, session, redirect, url_for
from random import choice

rawData = {
         "Jürgen Tamm": [143, '../static/friendata/img/1.jpg'],
         "Grethe Märts": [167, '../static/friendata/img/2.jpg'],
         "Hugo Vaher": [10, '../static/friendata/img/3.jpg'],
         "Päris Inimene": [486, '../static/friendata/img/4.jpg']}
""" 
rawData = {
         "1": [1, '../static/friendata/img/1.jpg'],
         "2": [2, '../static/friendata/img/2.jpg'],
         "3": [3, '../static/friendata/img/3.jpg'],
         "4": [4, '../static/friendata/img/4.jpg'],
         "5": [5, '../static/friendata/img/1.jpg'],
         "6": [6, '../static/friendata/img/2.jpg'],
         "7": [7, '../static/friendata/img/3.jpg'],
         "8": [8, '../static/friendata/img/4.jpg'],
         "9": [9, '../static/friendata/img/1.jpg'],
         "10": [10, '../static/friendata/img/2.jpg'],
         "11": [11, '../static/friendata/img/3.jpg'],
         "12": [12, '../static/friendata/img/4.jpg']} """

kasutajaNimi = 'Jürgen Tamm'
maxScore = len(rawData.keys())-1

app = Flask(__name__)
app.secret_key = b'41a2fc1a57d9edde2e44a19616490a330726f984ed7470953da97845c36224fb'
app.config['SESSION_COOKIE_SAMESITE'] = "Strict"

def randomSelect(viimaneNimi):
   while True:
      nimi = choice(list(session['people'].keys()))
      if nimi != kasutajaNimi and nimi != viimaneNimi:
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

   if nimi == 'kasutaja':
      randomFriend = randomSelect(nimi)
      return jsonify({'given': [kasutajaNimi, session['people'].pop(kasutajaNimi)], 'guess': [randomFriend, session['people'][randomFriend]], 'score': session['score']})
   else:
      session['score'] += 1
      if session['score'] == maxScore:
         return jsonify({'võit': 'jah', 'score': session['score']})

      randomFriend = randomSelect(nimi)
      return jsonify({'given': [nimi, session['people'].pop(nimi)], 'guess': [randomFriend, session['people'][randomFriend]], 'score': session['score']})
      


if __name__ == '__main__':
   app.run(debug = True)
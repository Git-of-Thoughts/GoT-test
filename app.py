from flask import Flask, render_template, request, redirect, url_for
from firebase_admin import initialize_app, auth, firestore
from user import User
from game import Game

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        User.register(request.form)
        return redirect(url_for('home'))
    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        User.login(request.form)
        return redirect(url_for('home'))
    return render_template('login.html')

@app.route('/game', methods=['GET', 'POST'])
def game():
    if request.method == 'POST':
        Game.start(request.form)
        return redirect(url_for('game'))
    return render_template('game.html')

if __name__ == '__main__':
    app.run(debug=True)

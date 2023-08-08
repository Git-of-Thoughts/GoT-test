from flask import Flask, render_template, request, redirect, url_for
from firebase_service import FirebaseService
from chess import ChessGame

app = Flask(__name__)
firebase_service = FirebaseService()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/game')
def game():
    return render_template('game.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = firebase_service.authenticate_user(email, password)
        if user:
            return redirect(url_for('game'))
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = firebase_service.create_user(email, password)
        if user:
            return redirect(url_for('login'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)

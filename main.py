from flask import Flask, request, render_template
from game import Game
from user import User
from database import Database

app = Flask(__name__)
game = Game()
db = Database()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        score = request.form.get('score')
        ip = request.remote_addr
        user = User(ip)
        db.update_score(user, score)
    return render_template('index.html')

@app.route('/ranking/<country>')
def ranking(country):
    ranking = db.get_ranking(country)
    return render_template('ranking.html', ranking=ranking)

if __name__ == '__main__':
    app.run(debug=True)

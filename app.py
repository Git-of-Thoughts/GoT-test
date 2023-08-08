from flask import Flask, jsonify
from greeting import Greeting

app = Flask(__name__)

@app.route('/')
def hello_world():
    greeting = Greeting()
    return jsonify(greeting.message())

if __name__ == '__main__':
    app.run(debug=True)

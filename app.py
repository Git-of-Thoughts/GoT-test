from flask import Flask, render_template
import json

app = Flask(__name__)

@app.route('/')
def home():
    with open('dinosaurs.json', 'r') as f:
        dinosaurs = json.load(f)
    return render_template('index.html', dinosaurs=dinosaurs)

if __name__ == '__main__':
    app.run(debug=True)

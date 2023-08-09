from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # This function will be called when the user navigates to the home page.
    # It will render the index.html template.
    return render_template('index.html')

if __name__ == '__main__':
    # This will start the server if the script is run directly.
    app.run(debug=True)

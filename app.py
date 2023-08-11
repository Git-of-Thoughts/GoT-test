from flask import Flask, request, jsonify
from database import get_customer, add_customer, update_customer, delete_customer, get_interaction, add_interaction, update_interaction, delete_interaction

app = Flask(__name__)

@app.route('/customer', methods=['GET', 'POST'])
def customer():
    if request.method == 'GET':
        return jsonify(get_customer(request.args.get('id')))
    elif request.method == 'POST':
        return jsonify(add_customer(request.json))

@app.route('/customer/<id>', methods=['PUT', 'DELETE'])
def customer_id(id):
    if request.method == 'PUT':
        return jsonify(update_customer(id, request.json))
    elif request.method == 'DELETE':
        return jsonify(delete_customer(id))

@app.route('/interaction', methods=['GET', 'POST'])
def interaction():
    if request.method == 'GET':
        return jsonify(get_interaction(request.args.get('id')))
    elif request.method == 'POST':
        return jsonify(add_interaction(request.json))

@app.route('/interaction/<id>', methods=['PUT', 'DELETE'])
def interaction_id(id):
    if request.method == 'PUT':
        return jsonify(update_interaction(id, request.json))
    elif request.method == 'DELETE':
        return jsonify(delete_interaction(id))

if __name__ == '__main__':
    app.run(debug=True)

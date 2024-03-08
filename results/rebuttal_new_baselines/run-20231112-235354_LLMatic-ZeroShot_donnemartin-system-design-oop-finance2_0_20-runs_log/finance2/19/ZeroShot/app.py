from flask import Flask, request, jsonify
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class User:
	id: str
	username: str
	password: str

@dataclass
class Account:
	id: str
	user_id: str
	balance: float

@dataclass
class Transaction:
	id: str
	account_id: str
	amount: float
	category: str

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE[user.id] = json.dumps(user.__dict__)
	return jsonify(user.__dict__), 201

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	account = Account(**data)
	DATABASE[account.id] = json.dumps(account.__dict__)
	return jsonify(account.__dict__), 201

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	DATABASE[transaction.id] = json.dumps(transaction.__dict__)
	return jsonify(transaction.__dict__), 201

if __name__ == '__main__':
	app.run(debug=True)

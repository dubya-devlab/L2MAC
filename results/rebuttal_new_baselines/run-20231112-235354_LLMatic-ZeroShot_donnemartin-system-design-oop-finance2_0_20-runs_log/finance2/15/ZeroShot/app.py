from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DB = {}

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
	DB['users'][user.id] = user
	return jsonify(user), 201

@app.route('/create_account', methods=['POST'])
def create_account():
	data = request.get_json()
	account = Account(**data)
	DB['accounts'][account.id] = account
	return jsonify(account), 201

@app.route('/create_transaction', methods=['POST'])
def create_transaction():
	data = request.get_json()
	transaction = Transaction(**data)
	DB['transactions'][transaction.id] = transaction
	return jsonify(transaction), 201

if __name__ == '__main__':
	app.run(debug=True)

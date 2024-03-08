from flask import Flask, request, jsonify
from dataclasses import dataclass
import json

app = Flask(__name__)

# Mock database
users = {}
messages = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	profile_picture: str = None
	status_message: str = None
	privacy_settings: dict = None

@dataclass
class Message:
	from_user: str
	to_user: str
	message: str
	read: bool = False

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	user = User(**data)
	users[user.email] = user
	return jsonify({'message': 'User registered successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	email = data.get('email')
	password = data.get('password')
	user = users.get(email)
	if not user or user.password != password:
		return jsonify({'message': 'Invalid email or password'}), 401
	return jsonify({'message': 'Logged in successfully'}), 200

@app.route('/message', methods=['POST'])
def send_message():
	data = request.get_json()
	message = Message(**data)
	messages.setdefault(message.from_user, []).append(message)
	return jsonify({'message': 'Message sent successfully'}), 201

@app.route('/message', methods=['GET'])
def get_messages():
	from_user = request.args.get('from_user')
	to_user = request.args.get('to_user')
	user_messages = messages.get(from_user, [])
	filtered_messages = [message for message in user_messages if message.to_user == to_user]
	return jsonify([message.__dict__ for message in filtered_messages]), 200

if __name__ == '__main__':
	app.run(debug=True)

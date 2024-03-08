import dataclasses
from flask import Flask, request, jsonify
from dataclasses import dataclass
from typing import Dict

app = Flask(__name__)

# Mock database
users = {}
files = {}

@dataclass
class User:
	name: str
	email: str
	password: str
	storage_used: int = 0

@dataclass
class File:
	name: str
	size: int
	owner: str
	versions: list = dataclasses.field(default_factory=list)

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

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	email = data.get('email')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	# In a real application, we would send an email to the user with a password reset link
	return jsonify({'message': 'Password reset link sent'}), 200

@app.route('/profile', methods=['GET'])
def profile():
	data = request.get_json()
	email = data.get('email')
	user = users.get(email)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	return jsonify(user.__dict__), 200

@app.route('/change_password', methods=['POST'])
def change_password():
	data = request.get_json()
	email = data.get('email')
	old_password = data.get('old_password')
	new_password = data.get('new_password')
	user = users.get(email)
	if not user or user.password != old_password:
		return jsonify({'message': 'Invalid email or old password'}), 401
	user.password = new_password
	return jsonify({'message': 'Password changed successfully'}), 200

@app.route('/upload_file', methods=['POST'])
def upload_file():
	data = request.get_json()
	file = File(**data)
	user = users.get(file.owner)
	if not user:
		return jsonify({'message': 'User not found'}), 404
	user.storage_used += file.size
	files[file.name] = file
	return jsonify({'message': 'File uploaded successfully'}), 201

@app.route('/download_file', methods=['GET'])
def download_file():
	data = request.get_json()
	file_name = data.get('file_name')
	file = files.get(file_name)
	if not file:
		return jsonify({'message': 'File not found'}), 404
	# In a real application, we would return the file content
	return jsonify(file.__dict__), 200

if __name__ == '__main__':
	app.run(debug=True)

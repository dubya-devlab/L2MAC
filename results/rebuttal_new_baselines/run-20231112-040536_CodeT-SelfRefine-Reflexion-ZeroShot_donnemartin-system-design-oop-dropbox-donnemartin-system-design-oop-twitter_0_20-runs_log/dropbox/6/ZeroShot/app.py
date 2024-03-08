from flask import Flask, request, jsonify
from dataclasses import dataclass
import user_management
import file_management
import file_sharing

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
	data = request.get_json()
	return jsonify(user_management.register(data))

@app.route('/login', methods=['POST'])
def login():
	data = request.get_json()
	return jsonify(user_management.login(data))

@app.route('/forgot_password', methods=['POST'])
def forgot_password():
	data = request.get_json()
	return jsonify(user_management.forgot_password(data))

@app.route('/profile', methods=['GET'])
def profile():
	data = request.get_json()
	return jsonify(user_management.profile(data))

@app.route('/change_password', methods=['POST'])
def change_password():
	data = request.get_json()
	return jsonify(user_management.change_password(data))

@app.route('/upload_file', methods=['POST'])
def upload_file():
	data = request.get_json()
	return jsonify(file_management.upload_file(data))

@app.route('/download_file', methods=['GET'])
def download_file():
	data = request.get_json()
	return jsonify(file_management.download_file(data))

@app.route('/organize_file', methods=['POST'])
def organize_file():
	data = request.get_json()
	return jsonify(file_management.organize_file(data))

@app.route('/version_file', methods=['GET'])
def version_file():
	data = request.get_json()
	return jsonify(file_management.version_file(data))

@app.route('/share_file', methods=['POST'])
def share_file():
	data = request.get_json()
	return jsonify(file_sharing.share_file(data))

@app.route('/shared_folder', methods=['POST'])
def shared_folder():
	data = request.get_json()
	return jsonify(file_sharing.shared_folder(data))

if __name__ == '__main__':
	app.run(debug=True)

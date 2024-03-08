from flask import Flask, request, jsonify
from dataclasses import dataclass

app = Flask(__name__)

# Mock database
DATABASE = {}

@dataclass
class User:
	id: str
	name: str
	email: str
	clubs: list

@dataclass
class Club:
	id: str
	name: str
	description: str
	is_private: bool
	members: list

@app.route('/create_user', methods=['POST'])
def create_user():
	data = request.get_json()
	user = User(**data)
	DATABASE[user.id] = user
	return jsonify(user), 201

@app.route('/create_club', methods=['POST'])
def create_club():
	data = request.get_json()
	club = Club(**data)
	DATABASE[club.id] = club
	return jsonify(club), 201

@app.route('/join_club', methods=['POST'])
def join_club():
	data = request.get_json()
	user_id = data['user_id']
	club_id = data['club_id']
	user = DATABASE[user_id]
	club = DATABASE[club_id]
	if club.is_private:
		return jsonify({'message': 'This club is private.'}), 403
	user.clubs.append(club_id)
	club.members.append(user_id)
	return jsonify({'message': 'Successfully joined the club.'}), 200

if __name__ == '__main__':
	app.run(debug=True)

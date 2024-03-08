import pytest
import app
from user import User
from chat import Chat

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['email'] == 'test@test.com'


def test_login(client):
	response = client.post('/register', json={'email': 'test@test.com', 'password': 'password'})
	data = response.get_json()
	user_id = data['id']
	response = client.post('/login', json={'email': 'test@test.com', 'password': 'password'})
	assert response.status_code == 200
	data = response.get_json()
	assert data['id'] == user_id
	assert data['email'] == 'test@test.com'


def test_create_chat(client):
	response = client.post('/chat', json={'name': 'Test Chat'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['name'] == 'Test Chat'
	assert data['messages'] == []


def test_send_message(client):
	chat = Chat('Test Chat')
	app.chats[chat.id] = chat
	response = client.post(f'/chat/{chat.id}/message', json={'user_id': '1', 'content': 'Hello, world!'})
	assert response.status_code == 201
	data = response.get_json()
	assert 'id' in data
	assert data['user_id'] == '1'
	assert data['content'] == 'Hello, world!'

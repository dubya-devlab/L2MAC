import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def token():
	return jwt.encode({'username': 'test'}, 'secret', algorithm='HS256')

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

def test_login(client):
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()

def test_profile_get(client, token):
	response = client.get('/profile', json={'token': token})
	assert response.status_code == 200

def test_profile_post(client, token):
	response = client.post('/profile', json={'token': token, 'profile': {'bio': 'test bio'}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}

def test_post(client, token):
	response = client.post('/post', json={'token': token, 'content': 'test post'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created successfully'}

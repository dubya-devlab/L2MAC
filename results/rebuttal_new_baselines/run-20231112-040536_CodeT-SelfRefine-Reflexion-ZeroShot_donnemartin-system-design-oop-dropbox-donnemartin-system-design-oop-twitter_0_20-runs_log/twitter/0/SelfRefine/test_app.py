import pytest
import app
import jwt

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'User registered successfully'}

	response = client.post('/register', json={'username': 'test', 'password': 'test', 'email': 'test@test.com'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'User already exists'}

	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'token' in response.get_json()

	response = client.post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Invalid username or password'}

	token = response.get_json()['token']
	response = client.put('/profile', json={'token': token, 'profile': {'name': 'Test User'}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Profile updated successfully'}

	response = client.post('/post', json={'token': token, 'post': {'title': 'Test Post', 'content': 'Test Content'}})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Post created successfully'}

	response = client.get('/posts', json={'token': token})
	assert response.status_code == 200
	assert 'posts' in response.get_json()

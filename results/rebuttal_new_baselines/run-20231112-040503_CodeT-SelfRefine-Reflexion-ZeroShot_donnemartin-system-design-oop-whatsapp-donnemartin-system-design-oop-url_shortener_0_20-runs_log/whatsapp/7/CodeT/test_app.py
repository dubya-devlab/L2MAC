import pytest
import app
import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json()['message'] == 'User created successfully'

	response = client.post('/signup', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Email already exists'


def test_login_logout(client):
	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged in successfully'

	response = client.post('/logout', data=json.dumps({'email': 'test@example.com'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json()['message'] == 'Logged out successfully'

	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'wrongpassword'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json()['message'] == 'Invalid email or password'

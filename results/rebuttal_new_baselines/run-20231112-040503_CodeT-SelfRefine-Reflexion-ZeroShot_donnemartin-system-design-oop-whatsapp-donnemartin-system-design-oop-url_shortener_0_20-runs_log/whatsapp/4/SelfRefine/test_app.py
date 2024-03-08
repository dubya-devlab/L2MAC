import pytest
import json
from app import app, db, User

@pytest.fixture
def client():
	app.config['TESTING'] = True
	with app.test_client() as client:
		yield client


def test_signup(client):
	response = client.post('/signup', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == {'message': 'User created successfully'}

	response = client.post('/signup', data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 400
	assert response.get_json() == {'message': 'Email already in use'}


def test_login(client):
	response = client.post('/login', data=json.dumps({'email': 'test@example.com', 'password': 'password'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged in successfully'}


def test_logout(client):
	response = client.post('/logout', data=json.dumps({'email': 'test@example.com'}), content_type='application/json')
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Logged out successfully'}


def test_forgot_password(client):
	response = client.post('/forgot_password', data=json.dumps({'email': 'test@example.com'}), content_type='application/json')
	assert response.status_code == 200
	assert 'new_password' in response.get_json()
	assert response.get_json()['message'] == 'Password reset successfully'

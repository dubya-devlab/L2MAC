import pytest
import app
from flask import json
import uuid

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 201
	assert 'user_id' in response.get_json()
	response = client.post('/register', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 400
	assert 'message' in response.get_json()


def test_login(client):
	client.post('/register', json={'username': str(uuid.uuid4()), 'password': 'test'})
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	assert 'access_token' in response.get_json()


def test_shorten_url(client):
	response = client.post('/register', json={'username': str(uuid.uuid4()), 'password': 'test'})
	user_id = response.get_json()['user_id']
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = response.get_json()['access_token']
	response = client.post('/shorten_url', json={'original_url': 'http://google.com', 'user_id': user_id}, headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 201
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/register', json={'username': str(uuid.uuid4()), 'password': 'test'})
	user_id = response.get_json()['user_id']
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = response.get_json()['access_token']
	response = client.post('/shorten_url', json={'original_url': 'http://google.com', 'user_id': user_id}, headers={'Authorization': f'Bearer {access_token}'})
	short_url = response.get_json()['short_url']
	url_id = short_url.split('/')[-1]
	response = client.get(f'/{url_id}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/register', json={'username': str(uuid.uuid4()), 'password': 'test'})
	user_id = response.get_json()['user_id']
	response = client.post('/login', json={'username': 'test', 'password': 'test'})
	access_token = response.get_json()['access_token']
	response = client.post('/shorten_url', json={'original_url': 'http://google.com', 'user_id': user_id}, headers={'Authorization': f'Bearer {access_token}'})
	short_url = response.get_json()['short_url']
	url_id = short_url.split('/')[-1]
	client.get(f'/{url_id}')
	response = client.get(f'/analytics/{url_id}', headers={'Authorization': f'Bearer {access_token}'})
	assert response.status_code == 200
	assert 'clicks' in response.get_json()

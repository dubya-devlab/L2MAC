import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	response = client.post('/create_user')
	assert response.status_code == 201
	assert 'user_id' in json.loads(response.data)


def test_create_url(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'user_id': user_id})
	assert response.status_code == 201
	assert 'url_id' in json.loads(response.data)
	assert 'short_url' in json.loads(response.data)


def test_redirect_url(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'user_id': user_id})
	short_url = json.loads(response.data)['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/create_user')
	user_id = json.loads(response.data)['user_id']
	response = client.post('/create_url', json={'original_url': 'https://www.google.com', 'user_id': user_id})
	url_id = json.loads(response.data)['url_id']
	response = client.get('/analytics', json={'url_id': url_id})
	assert response.status_code == 200
	assert 'clicks' in json.loads(response.data)
	assert 'click_data' in json.loads(response.data)

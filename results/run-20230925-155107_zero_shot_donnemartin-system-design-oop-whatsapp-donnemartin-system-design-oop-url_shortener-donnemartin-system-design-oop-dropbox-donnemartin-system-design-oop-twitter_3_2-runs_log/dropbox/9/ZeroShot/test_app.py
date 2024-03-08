import pytest
import app
from user import User
from file import File

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_register(client):
	response = client.post('/register', json={'name': 'Test User', 'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}


def test_login(client):
	response = client.post('/login', json={'email': 'test@example.com', 'password': 'password'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Test User', 'email': 'test@example.com', 'password': 'password'}


def test_upload(client):
	response = client.post('/upload', json={'name': 'Test File', 'type': 'text/plain', 'size': 100, 'content': 'Hello, World!'})
	assert response.status_code == 201
	assert response.get_json() == {'name': 'Test File', 'type': 'text/plain', 'size': 100, 'content': 'Hello, World!'}


def test_download(client):
	response = client.get('/download', query_string={'name': 'Test File'})
	assert response.status_code == 200
	assert response.get_json() == {'name': 'Test File', 'type': 'text/plain', 'size': 100, 'content': 'Hello, World!'}

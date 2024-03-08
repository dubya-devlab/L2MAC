import pytest
import app
import jwt

def test_register():
	app.users = {}
	response = app.app.test_client().post('/register', json={'username': 'test', 'email': 'test@test.com', 'password': 'test'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Registered successfully'}
	assert 'test' in app.users

def test_login():
	app.users = {'test': app.User('test', 'test@test.com', 'test', {})}
	response = app.app.test_client().post('/login', json={'username': 'test', 'password': 'test'})
	assert response.status_code == 200
	data = response.get_json()
	assert 'token' in data
	decoded = jwt.decode(data['token'], app.SECRET_KEY)
	assert decoded['user'] == 'test'

	response = app.app.test_client().post('/login', json={'username': 'test', 'password': 'wrong'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

	response = app.app.test_client().post('/login', json={'username': 'wrong', 'password': 'test'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Invalid username or password'}

def test_post():
	app.users = {'test': app.User('test', 'test@test.com', 'test', {})}
	app.posts = {}
	token = jwt.encode({'user': 'test', 'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}, app.SECRET_KEY)
	response = app.app.test_client().post('/post', json={'token': token, 'content': 'Hello, world!'})
	assert response.status_code == 200
	assert response.get_json() == {'message': 'Posted successfully'}
	assert len(app.posts) == 1
	assert app.posts[0].content == 'Hello, world!'

	response = app.app.test_client().post('/post', json={'content': 'Hello, world!'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Token is missing'}

	response = app.app.test_client().post('/post', json={'token': 'wrong', 'content': 'Hello, world!'})
	assert response.status_code == 401
	assert response.get_json() == {'message': 'Token is invalid'}

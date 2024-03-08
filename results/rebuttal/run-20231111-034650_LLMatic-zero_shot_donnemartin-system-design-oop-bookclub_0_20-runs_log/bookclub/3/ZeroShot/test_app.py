import pytest
import app
from app import User, Club, Book, Meeting, Discussion

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

def test_create_user(client):
	response = client.post('/user', json={
		'id': '1',
		'name': 'Test User',
		'email': 'test@example.com',
		'clubs': [],
		'books_read': [],
		'wish_list': [],
		'follows': []
	})
	assert response.status_code == 201
	assert isinstance(response.get_json(), dict)
	assert response.get_json()['name'] == 'Test User'

def test_create_club(client):
	response = client.post('/club', json={
		'id': '1',
		'name': 'Test Club',
		'description': 'This is a test club.',
		'is_private': False,
		'members': [],
		'books': [],
		'meetings': [],
		'discussions': []
	})
	assert response.status_code == 201
	assert isinstance(response.get_json(), dict)
	assert response.get_json()['name'] == 'Test Club'

def test_create_book(client):
	response = client.post('/book', json={
		'id': '1',
		'title': 'Test Book',
		'author': 'Test Author',
		'summary': 'This is a test book.',
		'reviews': []
	})
	assert response.status_code == 201
	assert isinstance(response.get_json(), dict)
	assert response.get_json()['title'] == 'Test Book'

def test_create_meeting(client):
	response = client.post('/meeting', json={
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'date': '2022-12-31',
		'reminder': True
	})
	assert response.status_code == 201
	assert isinstance(response.get_json(), dict)
	assert response.get_json()['date'] == '2022-12-31'

def test_create_discussion(client):
	response = client.post('/discussion', json={
		'id': '1',
		'club_id': '1',
		'book_id': '1',
		'user_id': '1',
		'message': 'This is a test discussion.',
		'replies': []
	})
	assert response.status_code == 201
	assert isinstance(response.get_json(), dict)
	assert response.get_json()['message'] == 'This is a test discussion.'

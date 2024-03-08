import pytest
import app
from app import Event

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client

@pytest.fixture
def sample_event():
	return Event(id=1, type='Birthday', date='2022-12-12', time='18:00', theme='Space', color_scheme='Blue')


def test_create_event(client, sample_event):
	response = client.post('/event', json=sample_event.__dict__)
	assert response.status_code == 201
	assert response.get_json() == sample_event.__dict__


def test_get_event(client, sample_event):
	app.DB[sample_event.id] = sample_event
	response = client.get(f'/event/{sample_event.id}')
	assert response.status_code == 200
	assert response.get_json() == sample_event.__dict__


def test_get_event_not_found(client):
	response = client.get('/event/999')
	assert response.status_code == 404
	assert response.get_json() == {'error': 'Event not found'}

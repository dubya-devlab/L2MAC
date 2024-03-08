import pytest
import app
from app import Event, Venue, Guest, Vendor

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	response = client.post('/event', json={'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	assert response.get_json() == {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}


def test_get_event(client):
	response = client.get('/event/1')
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'}


def test_update_event(client):
	response = client.put('/event/1', json={'id': 1, 'type': 'Wedding', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Beach', 'color_scheme': 'White'})
	assert response.status_code == 200
	assert response.get_json() == {'id': 1, 'type': 'Wedding', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Beach', 'color_scheme': 'White'}


def test_delete_event(client):
	response = client.delete('/event/1')
	assert response.status_code == 204

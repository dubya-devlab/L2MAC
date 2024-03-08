import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_event(client):
	response = client.post('/event', json={'type': 'Birthday', 'date': '2022-12-12', 'time': '18:00', 'theme': 'Space', 'color_scheme': 'Blue'})
	assert response.status_code == 201
	assert 'id' in json.loads(response.data)


def test_get_event(client):
	response = client.post('/event', json={'type': 'Wedding', 'date': '2022-12-25', 'time': '12:00', 'theme': 'Winter', 'color_scheme': 'White'})
	id = json.loads(response.data)['id']
	response = client.get(f'/event/{id}')
	assert response.status_code == 200
	assert json.loads(response.data)['type'] == 'Wedding'

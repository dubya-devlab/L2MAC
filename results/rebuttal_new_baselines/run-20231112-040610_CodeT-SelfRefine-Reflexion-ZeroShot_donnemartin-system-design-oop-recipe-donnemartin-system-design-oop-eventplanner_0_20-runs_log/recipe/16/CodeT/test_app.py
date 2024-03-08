import pytest
import app
from flask import json

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_create_user(client):
	data = {
		'id': '1',
		'name': 'Test User',
		'recipes': [],
		'favorites': []
	}
	response = client.post('/user', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == data


def test_create_recipe(client):
	data = {
		'id': '1',
		'name': 'Test Recipe',
		'ingredients': ['ingredient1', 'ingredient2'],
		'instructions': ['instruction1', 'instruction2'],
		'images': ['image1', 'image2'],
		'categories': ['category1', 'category2']
	}
	response = client.post('/recipe', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == data


def test_create_category(client):
	data = {
		'id': '1',
		'name': 'Test Category',
		'recipes': []
	}
	response = client.post('/category', data=json.dumps(data), content_type='application/json')
	assert response.status_code == 201
	assert response.get_json() == data

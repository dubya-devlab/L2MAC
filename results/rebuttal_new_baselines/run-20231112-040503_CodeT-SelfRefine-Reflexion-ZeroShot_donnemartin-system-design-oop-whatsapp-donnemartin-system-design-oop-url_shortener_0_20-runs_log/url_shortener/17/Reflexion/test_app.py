import pytest
import app

@pytest.fixture
def client():
	app.app.config['TESTING'] = True
	with app.app.test_client() as client:
		yield client


def test_shorten_url(client):
	response = client.post('/shorten', json={'long_url': 'https://www.google.com'})
	assert response.status_code == 200
	assert 'short_url' in response.get_json()


def test_redirect_url(client):
	response = client.post('/shorten', json={'long_url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/{short_url}')
	assert response.status_code == 302


def test_get_analytics(client):
	response = client.post('/shorten', json={'long_url': 'https://www.google.com'})
	short_url = response.get_json()['short_url']
	response = client.get(f'/analytics/{short_url}')
	assert response.status_code == 200
	assert 'clicks' in response.get_json()

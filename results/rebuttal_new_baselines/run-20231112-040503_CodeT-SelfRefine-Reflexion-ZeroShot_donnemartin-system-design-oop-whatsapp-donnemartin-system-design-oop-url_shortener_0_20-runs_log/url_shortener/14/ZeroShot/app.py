from flask import Flask, request, redirect, jsonify
from dataclasses import dataclass
from datetime import datetime
import uuid

app = Flask(__name__)

# Mock database
DB = {}

@dataclass
class URL:
	original: str
	shortened: str
	user: str
	clicks: list
	expiration: datetime

@app.route('/shorten', methods=['POST'])
def shorten_url():
	data = request.get_json()
	original_url = data.get('url')
	user = data.get('user')
	custom_short = data.get('custom')
	expiration = data.get('expiration')

	# Validate URL
	# TODO: Implement URL validation

	# Generate unique shortened URL
	short_url = custom_short if custom_short else str(uuid.uuid4())[:8]

	# Create URL object and store in DB
	url = URL(original=original_url, shortened=short_url, user=user, clicks=[], expiration=expiration)
	DB[short_url] = url

	return jsonify({'short_url': short_url}), 201

@app.route('/<short_url>', methods=['GET'])
def redirect_url(short_url):
	url = DB.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Check if URL has expired
	if url.expiration and url.expiration < datetime.now():
		return jsonify({'error': 'URL has expired'}), 410

	# Record click
	url.clicks.append({'timestamp': datetime.now().isoformat()})

	# Redirect to original URL
	return redirect(url.original, code=302)

@app.route('/analytics/<short_url>', methods=['GET'])
def get_analytics(short_url):
	url = DB.get(short_url)
	if not url:
		return jsonify({'error': 'URL not found'}), 404

	# Return analytics data
	return jsonify({'clicks': url.clicks}), 200

if __name__ == '__main__':
	app.run(debug=True)

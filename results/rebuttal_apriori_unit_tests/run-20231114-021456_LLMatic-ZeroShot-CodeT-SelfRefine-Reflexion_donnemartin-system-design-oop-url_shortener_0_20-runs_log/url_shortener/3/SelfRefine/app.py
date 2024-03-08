from flask import Flask, request, redirect
from dataclasses import dataclass
from datetime import datetime
import random
import string
import sqlite3

app = Flask(__name__)

# Database connection
conn = sqlite3.connect('database.db')
c = conn.cursor()

# Create tables
try:
	c.execute('''CREATE TABLE users
				(username text, password text)''')
	c.execute('''CREATE TABLE urls
				(original text, shortened text, expiration text, clicks integer, click_dates text, click_geolocations text)''')
except:
	pass

@dataclass
class User:
	username: str
	password: str
	urls: dict

@dataclass
class URL:
	original: str
	shortened: str
	expiration: datetime
	clicks: int
	click_dates: list
	click_geolocations: list

@app.route('/shorten', methods=['POST'])
def shorten_url():
	# This function will handle URL shortening
	pass

@app.route('/<short_url>', methods=['GET'])
def redirect_to_url(short_url):
	# This function will handle URL redirection
	pass

@app.route('/analytics', methods=['GET'])
def get_analytics():
	# This function will handle analytics retrieval
	pass

@app.route('/user', methods=['POST'])
def create_user():
	# This function will handle user account creation
	pass

@app.route('/user/<username>', methods=['GET', 'PUT', 'DELETE'])
def manage_user(username):
	# This function will handle user account management
	pass

@app.route('/admin', methods=['POST'])
def create_admin():
	# This function will handle admin account creation
	pass

@app.route('/admin/<username>', methods=['GET', 'PUT', 'DELETE'])
def manage_admin(username):
	# This function will handle admin account management
	pass

if __name__ == '__main__':
	app.run(debug=True)

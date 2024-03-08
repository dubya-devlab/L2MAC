from datetime import datetime
from app import db, login_manager
from flask_login import UserMixin

@login_manager.user_loader
def load_user(user_id):
	return User.query.get(int(user_id))

class User(db.Model, UserMixin):
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.String(20), unique=True, nullable=False)
	password = db.Column(db.String(60), nullable=False)
	urls = db.relationship('Url', backref='creator', lazy=True)

class Url(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	original_url = db.Column(db.String(500), nullable=False)
	short_url = db.Column(db.String(20), unique=True, nullable=False)
	clicks = db.Column(db.Integer, default=0)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
	created_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	expires_at = db.Column(db.DateTime)
	clicks_data = db.relationship('Click', backref='url', lazy=True)

class Click(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	url_id = db.Column(db.Integer, db.ForeignKey('url.id'), nullable=False)
	clicked_at = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
	clicker_ip = db.Column(db.String(100))

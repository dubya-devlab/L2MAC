import pytest
from random import randint, choices
import string
from datetime import datetime, timedelta
from app import User, URL

# Helper Functions
def random_url():
	return f'https://example{randint(1000, 9999)}.com'

def random_username():
	return 'user' + ''.join(choices(string.ascii_lowercase + string.digits, k=5))

def random_slug():
	return ''.join(choices(string.ascii_lowercase + string.digits, k=8))

# Test Functions
class TestURLShorteningService:

	def test_input_url_shortening(self):
		# This test will be implemented later
		pass

	def test_url_validation(self):
		# This test will be implemented later
		pass

	def test_unique_shortened_url(self):
		# This test will be implemented later
		pass

	def test_custom_short_link(self):
		# This test will be implemented later
		pass

	def test_redirection(self):
		# This test will be implemented later
		pass

	def test_analytics_retrieval(self):
		# This test will be implemented later
		pass

	def test_user_account_functions(self):
		# This test will be implemented later
		pass

	def test_admin_functions(self):
		# This test will be implemented later
		pass

	def test_url_expiration(self):
		# This test will be implemented later
		pass

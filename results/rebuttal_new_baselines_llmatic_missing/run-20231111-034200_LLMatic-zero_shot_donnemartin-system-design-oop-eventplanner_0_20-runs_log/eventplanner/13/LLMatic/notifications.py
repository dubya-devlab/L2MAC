class Notification:
	def __init__(self):
		self.notifications = {}

	def send_notification(self, user_id, message):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(message)
		return True

	def set_reminder(self, user_id, reminder):
		if user_id not in self.notifications:
			self.notifications[user_id] = []
		self.notifications[user_id].append(reminder)
		return True

	def get_notifications(self, user_id):
		return self.notifications.get(user_id, [])

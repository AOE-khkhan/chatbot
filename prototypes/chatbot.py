from collections import namedtuple
from datetime import datetime

class Chatbot(object):
	message_history = []

	def __init__(self):
		pass

	def log_message(self, msg, origin):
		valid_origins = ['user', 'bot']
		message_status = namedtuple('status', ['msg', 'origin', 'timestamp'])

		if origin not in valid_origins:
			raise ValueError("invalid origin")

		message = (msg, origin, datetime.now())
		self.message_history.append(message)

	def respond(self):
		"""
		The bot recieves responds to a message.

		"""
		msg = self.create_response()
		self.log_message(msg, 'bot')

	def create_response(self):
		return 'I am a generic bot'

	def recieve(self, msg):
		self.log_message(msg, 'user')

	def get_message_history(self):
		return self.message_history


class Alice(Chatbot):
	def create_response(self):
		return 'Hello, My name is Alice!'


class ChatbotFactory(object):
	"""
	Use a name paramater for a specific bot. 

	Usage:
		botFactory = ChatbotFactory()
		alice = botFactory.create_chatbot(name='alice')
		default_bot = botFactory.create_chatbot()
	"""

	chatbot_repo = {'alice': Alice}

	def __init__(self):
		pass

	def create_chatbot(self, **kwargs):
		if 'name' in kwargs:
			requested_chatbot = kwargs['name']
			if requested_chatbot in self.chatbot_repo:
				return self.chatbot_repo[requested_chatbot]()
		else:
			return Chatbot()


if __name__ == '__main__':
	botFactory = ChatbotFactory()	

	alice = botFactory.create_chatbot(name='alice')

	alice.recieve('Hello, Alice!')
	print alice.respond()

	print alice.get_message_history()





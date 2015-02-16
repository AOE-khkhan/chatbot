from collections import namedtuple
from datetime import datetime

from interpreters import InterpreterFactory
from response_generators import ResponseGenerator
from action_selectors import ActionSelectorFactory

class Chatbot(object):
	""" Agent model that simulates dialog. It is an extension of a dialog 
	manager with improved functionality such as individualism and sophisticated
	goal evaluation functions. 

	This is a base class for designing more complicated chatbots, however,
	it will return a very basic chatbot for test purposes.

	"""

	message_history = []
	_meta = {}

	def __init__(self):
		actionSelectorFactory = ActionSelectorFactory()
		interpreterFactory = InterpreterFactory()

	def log_message(self, msg, origin):
		valid_origins = ['user', 'bot']
		message_status = namedtuple('status', ['msg', 'origin', 'timestamp'])

		if origin not in valid_origins:
			raise ValueError("invalid origin")

		message = (msg, origin, datetime.now())
		self.message_history.append(message)


	def respond(self):
		""" End point for response communication. Allows for post-processing
		of the response message.

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
	"""  A basic chatbot

	"""

	def create_response(self):
		return 'Hello, My name is Alice!'


class ChatbotFactory(object):
	""" Used to produce instances of the "Chatbot" class.

	Examples:
		>>> botFactory = ChatbotFactory()
		>>> alice = botFactory.create_chatbot(name='alice')
		>>> default_bot = botFactory.create_chatbot()

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


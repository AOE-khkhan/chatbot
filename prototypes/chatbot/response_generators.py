from interpreters import Interpreter

class ResponseGenerator(object):
	""" Takes an interpreted message and creates a response

	Accepts chatbot, interpreter object

	"""

	_last_message = None

	def __init__(self, meta):
		pass

	def generate(self, message=None):
		output = 'You said: ' + self._last_message
		return output


class ResponseGeneratorFactory(object):

	def __init__(self):
		return Generator()

from interpreters import Interpreter

class ResponseGenerator(object):
	""" Takes an interpreted message and creates a response

	Accepts chatbot, interpreter object

	"""

	def __init__(self, interpreter, profile):
		self.interpreter = interpreter
		self.profile = profile

	def generate(self, message=None):
		output = 'You said: ' + self._last_message
		return output


class ResponseGeneratorFactory(object):

	def __init__(self):
		return Generator()

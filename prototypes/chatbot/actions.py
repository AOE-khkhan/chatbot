def empty_func():
	pass

class Action:
	def __init__(self):
		self._message = ''
		self._reason = ''
		self._keywords = ''
		self._result = ''
		self._requirement = ''

		def print_action(word='hello world!'):
			print word

		def empty_action():
			pass

		self._action = print_action

	def act(self):
		self._action()

	@property		
	def message(self):
		return self._message

class Ask(Action):
	def __init__(self):
		pass

class FailureToUnderstand(Action):
	def __init__(self):
		self._message = "I don't understand your input"

class SayHello(Action):
	def __init__(self, name='user'):
		self._message = "Hello, user"
		self._action = empty_func
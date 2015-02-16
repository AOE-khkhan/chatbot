class Action:
	def __init__(self):
		self._message = ''
		self._reason = ''
		self._keywords = ''
		self._result = ''
		self._requirement = ''

		def print_action(word='hello world!'):
			print word

		self._action = print_action

	def act(self):
		self._action()

	@property		
	def message(self):
		return _message

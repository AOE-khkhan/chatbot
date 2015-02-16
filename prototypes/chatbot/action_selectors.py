#! /usr/bin/python

from response_generators import ResponseGenerator

class ActionSelector(object):
	""" 
	"""
	
	def __init__(self, interaction=None, profile=None):
		""" Chooses one or more actions based on inputs.

		Args:
			interaction: instance of InteractionRecord
			profile: instance of ProfileManager
		"""

		self._interaction = interaction
		self._profile = profile
		self._actions = [] 
		self.response_gen = ResponseGenerator()

	def get_options(self):
		pass

	def select_action(self):
		output = response_gen.generate(self._interaction, self._profile)

		return output

	def select_actions(self):
		pass


class ActionSelectorFactory(object):
	
	def __init__(self):
		pass

	@staticmethod
	def create(selector="default"):
		return ActionSelector();



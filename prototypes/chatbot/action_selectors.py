#! /usr/bin/python

from response_generators import ResponseGenerator
from actions import *

class ActionSelector(object):
	""" 
	"""
	
	def __init__(self, w_m, profile=None):
		""" Chooses one or more actions based on inputs.

		Args:
			w_m: instance of WorkingMemory
			profile: instance of ProfileManager
		"""

		self._w_m = w_m
		self._profile = profile
		self._actions = [] 

	def get_options(self):
		pass

	def select_action(self):
		""" Selects an action, executes it, and returns its message
		"""

		action = SayHello()
		action.act()
		output = action.message

		return output

	def select_actions(self):
		pass


class ActionSelectorFactory(object):
	
	def __init__(self):
		pass

	@staticmethod
	def create(selector="default"):
		return ActionSelector;



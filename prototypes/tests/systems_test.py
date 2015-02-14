#! /usr/bin/python

import unittest

from parsers import Parser
from interpreters import Interpreter
from generators import Generator

class DialogueSystemPipeline(unittest.TestCase):
	"""Tests the dialogue system pipeline

	Input -> Parser -> Interpreter -> Generator -> Output

	"""

	def setUp(self):
		pass

	def tearDown(self):
		pass

	def test_smoke_test(self):
		parser = Parser()
		interpreter = Interpreter()
		generator = Generator()

if __name__ == '__main__':
	unittest.main()


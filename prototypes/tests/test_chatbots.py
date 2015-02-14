import unittest
from chatbots import Chatbot, Alice, ChatbotFactory

class ChatbotTest(unittest.TestCase):
	def test_smoke_test(self):
		chatbot = Chatbot()

class AliceTest(unittest.TestCase):
	def test_smoke_test(self):
		alice = Alice()

		bot_factory = ChatbotFactory()
		alice_copy = bot_factory.create_chatbot(name='alice')

		self.assertTrue(isinstance(alice_copy, Alice))


if __name__ == '__main__':
	unittest.main()


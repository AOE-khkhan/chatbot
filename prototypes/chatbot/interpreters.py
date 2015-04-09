import unittest

from parsers import Parser

# For tests
from person_profile import BasicProfile

class KnowledgeBase(object):
    def __init__(self):
        self.insults = ['fuck', 'asshole', 'bitch']


class Interpreter(object):
    def __init__(self, profile, w_m):
        self.parser = Parser()
        self.profile = profile
        self.w_m = w_m
        self.k_b = KnowledgeBase()

    def interpret(self, stimulus):
        parsed_data = self.parser.parse(stimulus)

        if set(self.k_b.insults).intersection(set(parsed_data)):
            self.profile.emotions.set_factor('pleasure', -0.1, increment=True)


class InterpreterFactory(object):
    def __init__(self):
        pass

    def get_interpreter(self):
        return Interpreter()

class InterpreterTest(unittest.TestCase):

    def setUp(self):
        self.factory = InterpreterFactory()
        self.profile = BasicProfile()
        self.w_m = None
        self.interpreter = Interpreter(self.profile, self.w_m)

    def test_is_insulted(self):
        old_pleasure = self.profile.emotions.get_factor('pleasure')

        self.interpreter.interpret('fuck you')

        new_pleasure = self.profile.emotions.get_factor('pleasure')

        print(new_pleasure, old_pleasure)
        self.assertLess(new_pleasure, old_pleasure)


if __name__ == '__main__':
    unittest.main()
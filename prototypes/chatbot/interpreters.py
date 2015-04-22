import unittest

from working_memory import WorkingMemory
from knowledge_base.knowledge_base import KnowledgeBase

from parsers import Parser

# For tests
from person_profile import BasicProfile

class Interpreter(object):
    def __init__(self, w_m, profile):
        self.parser = Parser()
        self.profile = profile
        self.w_m = w_m
        self.k_b = KnowledgeBase()

    def interpret(self, stimulus):
        self.w_m.push_input()

        parsed_data = self.parser.parse(stimulus)

        classes = []
        for wrd in parsed_data:
            matched = self.k_b.match(wrd)
            if matched:
                classes.append(matched[0])

        for cls in classes:
            word_class = cls.get_word_class()
            if word_class == 'noun':
                self.w_m.percept.nouns.append(cls)
            elif word_class == 'verb':
                self.w_m.percept.verbs.append(cls)
            elif word_class == 'adjective':
                self.w_m.percept.adjectivs.append(cls)
            elif word_class == 'adverb':
                self.w_m.percept.adverbs.append(cls)



class InterpreterFactory(object):
    def __init__(self):
        pass

    def get_interpreter(self):
        return Interpreter

class InterpreterTest(unittest.TestCase):

    def setUp(self):
        self.factory = InterpreterFactory()
        self.profile = BasicProfile()
        self.w_m = WorkingMemory()
        self.interpreter = Interpreter(self.profile, self.w_m)

    def test_interpret(self):
        from knowledge_base.knowledge_base import Dog

        self.interpreter.interpret('A dog is an animal')
        self.assertTrue(Dog in self.w_m.percept.nouns)


if __name__ == '__main__':
    unittest.main()
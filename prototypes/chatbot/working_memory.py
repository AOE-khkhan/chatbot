from datetime import datetime
import unittest

class Percept(object):
    def __init__(self):
        self.subjects = []
        self.verbs = []
        self.nouns = []
        self.adjectives = []
        self.adverbs = []
        self.named_entities = []

class WorkingMemory(object):
    def __init__(self):
        """
        Note: 
            None => unknown
            '' => none was found

        """

        self.goal = None
        self.interlocutor = None
        self.action_history = []
        self.percept_history = []
        self.percept = Percept()

    def push_input(self): 
        """ Push immediate percept information to percept history with
        additional information

        """
        snapshot = dict()
        snapshot['percept'] = self.percept
        snapshot['source'] = self.interlocutor
        snapshot['timestamp'] = datetime.now()
        self.percept = Percept()

if __name__ == '__main__':
    pass



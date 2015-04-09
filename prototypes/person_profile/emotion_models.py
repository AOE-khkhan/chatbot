import unittest

from personality_models import DimensionalModel


class EmotionModel(DimensionalModel):
    """ made to mirror personality model """
    pass


class PadEmotionalModel(EmotionModel):
    def __init__(self):
        super(PadEmotionalModel, self).__init__()

        self.valid_factors = ['pleasure', 'arousal', 'dominance']
        self.model_name = 'PAD'
        
        self._init_factors()


class EmotionModelTest(unittest.TestCase):
    def setUp(self):
        self.em = EmotionModel()


class PadEmotionalModelTest(unittest.TestCase):
    def setUp(self):
        self.em = PadEmotionalModel()
        pass

    def test_valid_assignment(self):
        self.em.set_factor('pleasure', 0)
        self.em.set_factor('arousal', 0)
        self.em.set_factor('dominance', 0)

        self.em.set_factor('pleasure', 1)
        self.em.set_factor('arousal', 1)
        self.em.set_factor('dominance', 1)

    def test_invalid_assignment(self):
        with self.assertRaises(ValueError):
            self.em.set_factor('pleasure', -1)


if __name__ == '__main__':
    unittest.main()


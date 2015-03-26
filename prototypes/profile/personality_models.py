import unittest

class DimensionalModel(object):
    """
    Base class for dimensional representation of a person's personality.

    """

    def __init__(self):
        self.valid_factors = [] # cached version of self.factors.keys()
        self.model_name = None
        self.factors = {"happiness": 0, "sadness": 0}
        self.factor_validators = dict()

    def _init_factors(self):
        self.factors = dict(zip(self.valid_factors, [0] * len(self.valid_factors)))

    def _pre_check(func):
        def checked_func(self, factor, *args, **kwargs):
            if factor not in self.factors:
                raise ValueError("Incorrect factor in model: factor not found") 

            return func(self, factor, *args, **kwargs)

        return checked_func

    @_pre_check
    def get_factor(self, factor):
        return self.factors[factor]

    @_pre_check
    def set_factor(self, factor, value):
        if self._factor_value_check(factor, value):
            self.factors[factor] = value
        else:
            raise ValueError("Incorrect value for this model factor; validation failed")

    def _factor_value_check(self, factor, value):

        def default_validator(value):
            if value > 1 or value < 0:
                return False
            else:
                return True

        if factor not in self.factor_validators:
            validate = default_validator
        else:
            validate = self.factor_validators[factor]

        return validate(value)


class PersonalityModel(DimensionalModel):
    """Personality Model refactored to Dimensional Model"""
    pass
    

class BigFiveModel(PersonalityModel):
     """source: http://en.wikipedia.org/wiki/Big_Five_personality_traits
     """

     def __init__(self):
        super(BigFiveModel, self).__init__()

        self.valid_factors = ['openness', 
            'conscientiousness', 
            'extraversion', 
            'agreeableness', 
            'neuroticism']

        self.model_name = 'five factor'

        self._init_factors()


class PersonalityModelTest(unittest.TestCase):

    def setUp(self):
        self.pm = PersonalityModel()

    def test_invalid_factor_access(self):
        with self.assertRaises(ValueError):
            self.pm.get_factor('happyyyness')

    def test_valid_factor_access(self):
        self.assertEquals(self.pm.get_factor('happiness'), 0)

    def test_invalid_factor_value(self):
        with self.assertRaises(ValueError):
            self.pm.set_factor('happiness', 9000)

        self.pm.factor_validators['sadness'] = lambda x: x == 0

        self.pm.set_factor('sadness', 0) 

        with self.assertRaises(ValueError):
            self.pm.set_factor('sadness', 1)


class BigFiveModelTest(unittest.TestCase):

    def setUp(self):
        self.bfm = BigFiveModel()

    def test_assignment(self):
        self.bfm.set_factor('openness', 1)
        self.bfm.set_factor('conscientiousness', 1)
        self.bfm.set_factor('extraversion', 1)
        self.bfm.set_factor('neuroticism', 1)


if __name__ == '__main__':
    unittest.main()









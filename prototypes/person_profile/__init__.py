from person_profile.emotion_models import EmotionModel, PadEmotionalModel
from person_profile.personality_models import PersonalityModel, BigFiveModel

class PersonProfile(object):

    def __init__(self):
        self.emotions = EmotionModel()
        self.personality = PersonalityModel()

class BasicProfile(PersonProfile):

    def __init__(self):
        self.emotions = PadEmotionalModel()
        self.profile = BigFiveModel()

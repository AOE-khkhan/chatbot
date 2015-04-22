class KnowledgeBase(object):
    def all(self):
        return KbRoot.get_children()

    def match(self, pattern):
        """ 
        Returns: 
            list: A of classes that match the given pattern.

        """

        def normalize(name):
            name = name.lower()

            return name

        data = self.all()

        results = []

        for clsname, cls in data:
            if pattern in normalize(clsname): 
                results.append(cls)

        return results


class KbRoot(object):
    def __init__(self):
        self.category = None
        self.bull = 'hello'
        self.alt_spelling = []

    @classmethod
    def get_word_class(cls):
        return getattr(cls, '_word_class')

    def get_name(self):
        return self.__class__.__name__

    @staticmethod
    def get_children():
        def getc(cls):
                l = [(cls.__name__, cls)]
                alt_attr = "_" + cls.__class__.__name__ + '.__alts'
                if hasattr(cls, alt_attr):
                    l.extend([(wrd, cls) for wrd in cls.getattr(alt_attr)])
                for i in [getc(c) for c in cls.__subclasses__()]:
                    l.extend(i)

                return l

        result = getc(KbRoot)[1:] # Disclude "KB" class
        return result


class Animal(KbRoot):
    _word_class = 'noun'
    def __init__(self):
        pass

class Dog(Animal):
    _domesticated = True

    def __init__(self):
        super(Dog, self).__init__()


class GSD(Dog):
    def __init__(self):
        super(GSD, self).__init__()


class chiuaha(Dog):
    def __init__(self):
        super(chiuaha, self).__init__()


class Goat(Animal):
    _word_class = 'verb'

    def __init__(self):
        super(Goat, self).__init__()

class Verb(KbRoot):
    def __init__(self):
        super(Verb, self).__init__()

class Play(Verb):
    _word_class = 'verb'
    def __init__(self):
        super(Play, self)

class Ask(Verb):
    _word_class = 'verb'
    def __init__(self):
        super(Ask, self)

if __name__ == "__main__":
    kb = KnowledgeBase()
    print kb.all()


    dog = Dog()
    goat = Goat()
    animal = Animal()

    print 'dog', dir(dog)
    print 'goat', dir(goat)
    print 'animal', dir(animal)

    print kb.match('dog')
    d = kb.match('dog')[0]()
    g = kb.match('goat')[0]()
    print d.get_word_class()
    print g.get_word_class(), g.get_name()

    print dir(g)

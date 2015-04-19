class KnowledgeBase(object):
    def all(self):
        return KB.get_children()

    def match(self, pattern):

        def normalize(name):
            name = name.lower()

            return name

        data = self.all()

        results = []

        for clsname, cls in data:
            if pattern in normalize(clsname): 
                results.append(cls)

        return results


class KB(object):

    @staticmethod
    def get_children():
        def getc(cls):
                l = [(cls.__name__, cls)]
                for i in [getc(c) for c in cls.__subclasses__()]:
                    l.extend(i)

                return l

        result = getc(KB)[1:] # Disclude "KB" class
        return result


class Animal(Noun):
    def __init__(self):
        pass


class Dog(Animal):
    def __init__(self):
        pass


class GSD(Dog):
    def __init__(self):
        pass


class chiuaha(Dog):
    def __init__(self):
        pass


class Goat(Animal):
    def __init__(self):
        pass


if __name__ == "__main__":
    kb = KnowledgeBase()
    print kb.all()

    print kb.match('dog')

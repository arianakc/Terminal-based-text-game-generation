import sys


def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


characters = ['John', 'David', 'Jason']
clmapping = {'house': ["John", "Jason"], 'station': ['David']}
vehicles = ['SUV', 'truck']
locations = ['house', 'station']
almapping = {'house': ["eat", "drink"], 'station': ['park']}


class John(object):
    def __init__(self):
        self.dialogues = ["Hi, how are you?", "Do you feel very bad?"]
        self.name = "John"
        self.start_location = "house"


class David(object):
    def __init__(self):
        self.dialogues = ["You are amazing!", "You looks good, bro!"]
        self.name = "David"
        self.start_location = "station"


class Jason(object):
    def __init__(self):
        self.dialogues = ["Today is a wonderful day!", "You are a hero, bro!"]
        self.name = "Jason"
        self.start_location = "house"


class eat(object):
    def __init__(self):
        self.result = "You eat the food and it is delicious!"
        self.action = "eat"
        self.at_location = "house"


class drink(object):
    def __init__(self):
        self.result = "You drink the water and feel better!"
        self.action = "drink"
        self.at_location = "house"


class park(object):
    def __init__(self):
        self.result = "You park your vehicle!"
        self.action = "park"
        self.at_location = "station"

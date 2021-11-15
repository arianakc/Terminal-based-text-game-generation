characters = ['John', 'David', 'Jason', 'Mark', 'Mary', 'Anna']
clmapping = {'house': ["John", "Jason"], 'station': ['David'], 'airport': ["Mark"], "beach": ['Mary', "Anna"]}
lcmapping = {"John": 'house', "David": 'station', "Jason": "house", "Mark": "airport", 'Mary': "beach", "Anna": "beach"}
vehicles = ['SUV', 'truck', "taxi", "bus"]
locations = ['house', 'station', 'airport', "beach"]
almapping = {'house': ["eat", "drink"], 'station': ['park'], 'airport': ["check_in"], "beach": ["sleep"]}


class John(object):
    def __init__(self):
        self.dialogues = ["Hi, how are you?", "Do you feel very bad?"]
        self.name = "John"
        self.start_location = "house"
        self.current_location = "house"


class David(object):
    def __init__(self):
        self.dialogues = ["You are amazing!", "You looks good, bro!"]
        self.name = "David"
        self.start_location = "station"
        self.current_location = "station"


class Jason(object):
    def __init__(self):
        self.dialogues = ["Today is a wonderful day!", "You are a hero, bro!"]
        self.name = "Jason"
        self.start_location = "house"
        self.current_location = "house"


class Mark(object):
    def __init__(self):
        self.dialogues = ["Did you check in, bro?", "We do not accept you, sir!", "Do not take photo in the airport!"]
        self.name = "Mark"
        self.start_location = "airport"
        self.current_location = "airport"


class Mary(object):
    def __init__(self):
        self.dialogues = ["There is so much fun here!", "Can I call you back?"]
        self.name = "Mary"
        self.start_location = "beach"
        self.current_location = "beach"


class Anna(object):
    def __init__(self):
        self.dialogues = ["You are very handsome! May I have your phone number?", "Let's play together!"]
        self.name = "Anna"
        self.start_location = "beach"
        self.current_location = "beach"


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


class check_in(object):
    def __init__(self):
        self.result = "You checked in! Please go on board!"
        self.action = "check in"
        self.at_location = "airport"


class sleep(object):
    def __init__(self):
        self.result = "You lay down and have a good sleep on the beach."
        self.action = "sleep"
        self.at_location = "beach"

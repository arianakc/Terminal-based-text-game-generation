def generate_character(characters, dialogues):
    return "class Mark:\n    pass"


def generate_map(locations):
    return "class Location:\n    pass"


def generate_character_location_mappings(characters, map):
    return "class CLMapping:\n    pass"


def generate_actions(actions):
    return "class Action:\n    pass"


def generate_action_location_character_mappings(characters, map, actions):
    return "class ALCMapping:\n    pass"


def generate_prompt(prompts):
    return "def start():\n    pass"


def generate_game(characters, dialogues, locations, vehicles, prompts):
    characters = generate_character(characters, dialogues)
    map = generate_map(locations)
    codes = characters + "\n\n\n" + map
    vehicles = generate_actions(vehicles)
    codes = codes + "\n\n\n" + vehicles
    clmappings = generate_character_location_mappings(characters, map)
    codes = codes + "\n\n\n" + clmappings
    codes = codes + "\n\n\n" + generate_prompt(prompts)
    codes = codes + "\n\n\nif __name__ == '__main__':\n    print(\"Game start!\")\n    start()"
    return codes


def write(codes, filename="start_game.py"):
    with open(filename, "w") as code_file:
        code_file.write(codes)


if __name__ == '__main__':
    characters = ['John', 'David', 'brother', 'Katie', 'June', 'daughter', 'wife', 'Daddy', 'sweetie', 'anchorman',
                  'sir', 'John lay', 'body', 'John John', 'passenger', 'lady', 'son', 'driver', 'Carol', 'couple',
                  'Dan', 'speaker', 'John Hunt', 'June Hunt', 'John Hunt John Hunt']
    dialogues = [{"character1": ["", "", ""]}, {"character2": ["", "", ""]}]
    locations = ['Colorado', 'house', 'town', 'installation', 'west side', 'bunker', 'barbeque', 'John hand', 'room',
                 'kitchen', 'sky', 'New York City', 'counter', 'highway', 'road', 'ground', 'station', 'ramp',
                 'Wyoming', 'roadblock', 'Dan lap', 'compartment', 'block', 'torso', 'gate']
    vehicles = ['craft', 'SUV', 'vehicle', 'revolver', 'tank', 'SUV.He', 'truck']
    prompts = ["go to", "talk to", "observe", "take"]
    codes = generate_game(characters, dialogues, locations, vehicles, prompts)
    write(codes)

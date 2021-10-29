from example_code_gdl import *
from copy import deepcopy
import random
import time


def start():
    print("Game start!")
    while character := input(f"Please choose the character from the {characters}>>"):
        if character not in characters:
            print("There is no such character, please reinput!")
            continue
        character = str_to_class(character)()
        print(f"You are {character.name} and You are in {character.current_location}")
        while prompt := input(">>"):
            if prompt.startswith("go to"):
                target_location = prompt.split("go to ")[1]
                if target_location in locations:
                    if target_location == character.current_location:
                        print(f"You are already in {target_location}")
                    else:
                        while vehicle := input(f"please select vehicles to use from {vehicles}>>"):
                            if vehicle in vehicles:
                                print(f"You take {vehicle} to {target_location}. Have a good travel!")
                                print(f"traveling....")
                                time.sleep(3)
                                print(f"You achieve at {target_location}.")
                                clmapping[character.current_location].remove(character.name)
                                character.current_location = target_location
                                lcmapping[character.name] = target_location
                                clmapping[target_location].append(character.name)
                                break
                            else:
                                print("There is no such vehicle!")
                else:
                    print("There is no such location")
            elif prompt.startswith("talk to"):
                location_characters = deepcopy(clmapping[character.current_location])
                if character.name in location_characters:
                    location_characters.remove(character.name)
                target_character = prompt.split("talk to ")[1]
                if target_character in location_characters:
                    character_dialogues = str_to_class(target_character)().dialogues
                    if len(character_dialogues) > 0:
                        dialogue = random.choice(character_dialogues)
                        print(f"{target_character}:{dialogue}")
                    else:
                        print(f"{target_character} has nothing to talk!")
                else:
                    print(f"There is no {target_character} at {character.current_location}!")
            elif prompt.startswith("do"):
                location_actions = deepcopy(almapping[character.current_location])
                target_action = prompt.split("do ")[1]
                if target_action in location_actions:
                    action_result = str_to_class(target_action)().result
                    print(action_result)
                else:
                    print(f"You cannot {target_action} at {character.current_location}!")
            elif prompt.startswith("observe characters"):
                location_characters = deepcopy(clmapping[character.current_location])
                if character.name in location_characters:
                    location_characters.remove(character.name)
                if len(location_characters) > 0:
                    print(f"You found {location_characters} in {character.current_location}.")
                else:
                    print(f"There is no one at {character.current_location}")
            elif prompt.startswith("show actions"):
                location_actions = deepcopy(almapping[character.current_location])
                if len(location_actions) > 0:
                    print(f"You can take actions: {location_actions} in {character.current_location}.")
                else:
                    print(f"There is no action to take at {character.current_location}")
            elif prompt.startswith("observe locations"):
                location_list = deepcopy(locations)
                location_list.remove(character.current_location)
                if len(location_list) > 0:
                    print(f"You found locations: {location_list}!")
                else:
                    print(f"There is no other location!")
            elif prompt.lower().startswith("where am i"):
                print(f"You are in {character.current_location}!")
            elif prompt.lower().startswith("change character"):
                while new_character := input(f"Please choose the character from the {characters}>>"):
                    if new_character not in characters:
                        print("There is no such character, please reinput!")
                        continue
                    else:
                        character = str_to_class(new_character)()
                        character.current_location = lcmapping[character.name]
                        print(f"You are {character.name} and You are in {character.current_location}")
                        break
            elif prompt == "q":
                print("Bye!")
                exit(0)
            else:
                print("There is no such prompt, please reinput!")


if __name__ == '__main__':
    start()

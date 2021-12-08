from code_gdl_v3 import *
import random
import time
import os
import sys
import textwrap

wrapper = textwrap.TextWrapper(width=50)
def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


def say(message):
    os.system(f"say {message}")


def print_and_say(message):
    print(message)
    say(message)


def print_and_say_with_sex(message, voice="Alex"):
    print(message)
    os.system(f"say -v {voice} {message}")


def get_object_by_name(object_name, objects):
    for _object in objects:
        if _object.name == object_name:
            return _object


def get_actions_by_location(location):
    location_actions = []
    for action in all_actions:
        if location in action.locations:
            location_actions.append(action)
    return location_actions


def get_location_distance(target_location, location_distances):
    for location, distance in location_distances:
        if target_location == location:
            return distance


def get_characters_by_location(location):
    return [character for character in all_characters if character.current_location == location]


def check_quest_condition(character):
    if character.money >= win_money and character.hunger >= win_hunger and character.happiness >= win_happiness \
            and character.health > win_health:
        print_and_say("You successfully achieved game goals! Bye!")
        exit(0)
    elif character.health <= lose_health:
        print("Your current health is " + str(character.health))
        print("Your health cannot smaller than or equal to " + str(lose_health))
        print_and_say("You failed the game! Game over!")
        exit(0)
    elif character.money <= lose_money:
        print("Your current money is " + str(character.money))
        print("Your money cannot smaller than or equal to " + str(lose_money))
    elif character.happiness <= lose_happiness:
        print("Your current happiness is " + str(character.happiness))
        print("Your happiness cannot smaller than or equal to " + str(lose_happiness))
        print_and_say("You failed the game! Game over!")
        exit(0)
    elif character.hunger <= lose_hunger:
        print("Your current hunger is " + str(character.hunger))
        print("Your hunger cannot smaller than or equal to " + str(lose_hunger))
        print_and_say("You failed the game! Game over!")
        exit(0)
    else:
        print("\n------------current mystery quest status------------------")
        print("Your current health is " + str(character.health), f", the goal is {win_health} and",
              f"you will lose if smaller or equal to {lose_health}")
        print("Your current hunger is " + str(character.hunger), f", the goal is {win_hunger} and",
              f"you will lose if smaller or equal to {lose_hunger}")
        print("Your current money is " + str(character.money), f", the goal is {win_money} and",
              f"you will lose if smaller or equal to {lose_money}")
        print("Your current happiness is " + str(character.happiness), f", the goal is {win_happiness} and",
              f"you will lose if smaller or equal to {lose_happiness}")


def check_event_condition(events, operation):
    completed_events = []
    uncompleted_events = []
    for event in events:
        if event.judge_if_event_completed(operation):
            completed_events.append(event)
            if event.children is not None:
                uncompleted_events.extend(event.children)
        else:
            uncompleted_events.append(event)
    return completed_events, uncompleted_events



def show_events_instructions(scene_id, events):
    string = f"This is scene {scene_id}.\n"
    for event in events:
        string = string + "event "+str(event.event_id) + ":" + wrapper.fill(event.instruction) + "\n"
    return string

def start():
    print_and_say("Game start!")
    say("Please choose the mode")
    is_mysterybox_mode = None
    is_story_model = None
    while mode := input("Please choose the mode: 1.Exploration mode, 2.Mystery box mode 3.Story mode>>"):
        if int(mode) == 1:
            is_story_model = False
            is_mysterybox_mode = False
            break
        elif int(mode) == 2:
            is_mysterybox_mode = True
            is_story_model = False
            break
        elif int(mode) == 3:
            is_mysterybox_mode = False
            is_story_model = True
            break
        else:
            print_and_say("Your input is wrong! please reinput!")
            say("Please choose the mode")
    if is_mysterybox_mode:
        print_and_say("The mystery box quest enabled!")
    elif is_story_model:
        print_and_say("The story mode enabled!")
    else:
        print_and_say("Exploration mode enabled!")
    character_names = [character.name for character in characters]
    # location_names = [location.name for location in all_locations]
    if is_story_model:
        scene_id = 0
        current_scene = scenes[scene_id]
        current_events = current_scene.events
        character = characters[0]
        operation = None
        print_and_say(f"You are {character.name} and You are in {character.current_location.name}")
        while prompt := input(show_events_instructions(scene_id, current_events)+">>"):
            if prompt.startswith("go to"):
                nearby_location_distances = game_map.find_nearby_location(character.current_location)
                nearby_location_names = [location.name for location, distance in nearby_location_distances]
                nearby_locations = [location for location, distance in nearby_location_distances]
                target_location_name = prompt.split("go to ")[1]
                if target_location_name in nearby_location_names:
                    if target_location_name == character.current_location.name:
                        print_and_say(f"You are already in {target_location_name}")
                    else:
                        vehicle_names = [vehicle.name for vehicle in character.current_location.vehicles]
                        if len(vehicle_names) == 0:
                            say(f"You take walk to {target_location_name}.")
                            print_and_say(f"traveling....")
                            time.sleep(1)
                            target_location = get_object_by_name(target_location_name, nearby_locations)
                            operation = Operation(prompt="go to", target_location=target_location)
                            character.current_location = target_location
                            print_and_say(f"You achieve at {target_location_name}.")
                        else:
                            vehicle_names.append("walk")
                            say(f"please select vehicles to use from {vehicle_names}")
                            while vehicle_name := input(f"please select vehicles to use from {vehicle_names}>>"):
                                if vehicle_name in vehicle_names:
                                    if vehicle_name == "walk":
                                        say(f"You take walk to {target_location_name}.")
                                        print_and_say(f"traveling....")
                                        time.sleep(1)
                                        target_location = get_object_by_name(target_location_name, nearby_locations)
                                        operation = Operation(prompt="go to", target_location=target_location)
                                        character.current_location = target_location
                                        print_and_say(f"You achieve at {target_location_name}.")
                                        break
                                    else:
                                        print_and_say(
                                            f"You take {vehicle_name} to {target_location_name}. Have a good travel!")
                                        vehicle = get_object_by_name(vehicle_name, character.current_location.vehicles)
                                        character.current_location.vehicles.remove(vehicle)
                                        print_and_say(f"traveling....")
                                        time.sleep(2)
                                        target_location = get_object_by_name(target_location_name, nearby_locations)
                                        travel_distance = get_location_distance(target_location,
                                                                                nearby_location_distances)
                                        if is_mysterybox_mode:
                                            health_deduction, money_deduction, happiness_deduction, hunger_deduction \
                                                = vehicle.consume_properties(travel_distance)
                                            character.health -= int(health_deduction)
                                            print_and_say(f"You lose {int(health_deduction)} health during travel.")
                                            character.money -= int(money_deduction)
                                            print_and_say(f"You lose {int(money_deduction)} money during travel.")
                                            character.happiness -= int(happiness_deduction)
                                            print_and_say(
                                                f"You lose {int(happiness_deduction)} happiness during travel.")
                                            character.hunger -= int(hunger_deduction)
                                            print_and_say(f"You lose {int(hunger_deduction)} hunger during travel.")
                                            check_quest_condition(character)
                                        print_and_say(f"You achieve at {target_location_name}.")
                                        if vehicle not in target_location.vehicles:
                                            target_location.vehicles.append(vehicle)
                                        character.current_location = target_location
                                        operation = Operation(prompt="go to", target_location=target_location)
                                        break
                                else:
                                    print_and_say(f"There is no such vehicle in {character.current_location.name}")
                                    say(f"please select vehicles to use from {vehicle_names}")
                else:
                    print_and_say("There is no such location or You cannot direct achieve that location.")

            elif prompt.startswith("talk to"):
                location_characters = get_characters_by_location(character.current_location)
                target_character_name = prompt.split("talk to ")[1]
                location_characters_names = [c.name for c in location_characters if c != character]
                if target_character_name in location_characters_names:
                    target_character = get_object_by_name(target_character_name, location_characters)
                    operation = Operation(prompt="talk to", target_character=target_character)
                    event_dialogues = [event.dialogue for event in current_events]
                    for dialogue in event_dialogues:
                        if dialogue.npc == target_character:
                            for i in range(len(dialogue.sentences)):
                                speaker, sentence = dialogue.get_sentence_by_turn(i)
                                print(speaker.name+":")
                                print_and_say_with_sex(sentence, speaker.voice)
                            break
                else:
                    print_and_say(f"There is no {target_character_name} at {character.current_location}!")
                    operation=None
            elif prompt.startswith("do"):
                location_actions = get_actions_by_location(character.current_location)
                location_actions_names = [action.name for action in location_actions]
                target_action_item = prompt.split(" ")
                if len(target_action_item) == 3:
                    target_action = target_action_item[1]
                    target_item = target_action_item[2]
                elif len(target_action_item) == 2:
                    target_action = target_action_item[1]
                    target_item = None
                else:
                    target_action = None
                    target_item = None
                if target_action is None:
                    print_and_say(f"Your input format is wrong!")
                elif target_action in location_actions_names:
                    target_action = get_object_by_name(target_action, location_actions)
                    if target_item is not None and target_item not in all_character_items_names:
                        target_item = get_object_by_name(target_item, character.current_location.items)
                        character.conduct(target_action, item=target_item)
                    elif target_item is None:
                        character.conduct(target_action, item=target_item)
                    else:
                        print_and_say("There is no such item in the world!")
                    operation = Operation(prompt="do", action=target_action)
                else:
                    print_and_say(f"You cannot {target_action} at {character.current_location.name}!")

            elif prompt.startswith("use"):
                target_items_names = [item.name for item in character.items]
                target_item = prompt.split(" ")[1]
                if target_item in target_items_names:
                    target_item = get_object_by_name(target_item, character.items)
                    character.use(target_item)
                else:
                    print_and_say("There is no such item in you packet!")

            elif prompt.startswith("show characters"):
                location_characters = get_characters_by_location(character.current_location)
                if character in location_characters:
                    location_characters.remove(character)
                if len(location_characters) > 0:
                    location_characters_names = [character.name for character in location_characters]
                    print_and_say(f"You found {location_characters_names} in {character.current_location.name}.")
                else:
                    print_and_say(f"There is no one at {character.current_location.name}")
            elif prompt.startswith("show actions"):
                location_actions = get_actions_by_location(character.current_location)
                if len(location_actions) > 0:
                    location_actions_names = [action.name for action in location_actions]
                    print_and_say(
                        f"You can take actions: {location_actions_names} in {character.current_location.name}.")
                else:
                    print_and_say(f"There is no action to take at {character.current_location.name}")

            elif prompt.startswith("show locations"):
                nearby_location_distances = game_map.find_nearby_location(character.current_location)
                if len(nearby_location_distances) > 0:
                    location_names = [location.name for location, distance in nearby_location_distances]
                    print_and_say(f"You found nearby locations: {location_names}!")
                else:
                    print_and_say(f"There is no other location!")
            elif prompt.startswith("show map"):
                game_map.show(character.current_location)
            elif prompt.lower().startswith("where am i"):
                print_and_say(f"You are in {character.current_location.name}!")
            elif prompt.lower().startswith("who am i"):
                print_and_say(f"You are {character.name}!")
            elif prompt.lower().startswith("change character"):
                say(f"Please choose the character from the {character_names}")
                while new_character_name := input(f"Please choose the character from the {character_names}>>"):
                    if new_character_name not in character_names:
                        print_and_say("There is no such character, please reinput!")
                        say(f"Please choose the character from the {character_names}")
                        continue
                    else:
                        character = get_object_by_name(new_character_name, all_characters)
                        print_and_say(f"You are {character.name} and You are in {character.current_location.name}")
                        break
            elif prompt.lower().startswith("show status"):
                character.show_status()
            elif prompt.lower().startswith("show items"):
                character.show_items()
            elif prompt.lower().startswith("show objects"):
                message = f"You found objects in {character.current_location.name}: " + ", ".join(
                    [item.name for item in character.current_location.items])
                print_and_say(message)
            elif prompt == "q":
                print_and_say("Bye!")
                exit(0)
            else:
                print_and_say("There is no such prompt, please reinput!")
            if operation is not None:
                completed_events, uncompleted_events = check_event_condition(current_events, operation)
                for completed_event in completed_events:
                    if completed_event.end_text is not None:
                        print("----------------------------------------------------")
                        print(wrapper.fill(completed_event.end_text))
                        say(completed_event.end_text)
                    print_and_say(f"You completed the event {completed_event.event_id}.")
                current_events = uncompleted_events
                if len(current_events) == 0:
                    print_and_say(f"You completed the scene {scene_id}")
                    scene_id += 1
                    if scene_id == len(scenes):
                        print_and_say(f"You completed all scenes and this is the end of the story. Bye!")
                        exit(0)
                    current_scene = scenes[scene_id]
                    current_events = current_scene.events
                    if current_scene.refresh_location:
                        for c in current_events[0].characters:
                            c.current_location = current_scene.events[0].location
    else:
        say(f"Please choose the character from the {character_names}")
        while character := input(f"Please choose the character from the {character_names}>>"):
            if character not in character_names:
                print_and_say("There is no such character, please reinput!")
                say(f"Please choose the character from the {character_names}")
                continue
            character = get_object_by_name(character, all_characters)
            print_and_say(f"You are {character.name} and You are in {character.current_location.name}")
            if is_mysterybox_mode:
                check_quest_condition(character)
            while prompt := input(">>"):
                if prompt.startswith("go to"):
                    nearby_location_distances = game_map.find_nearby_location(character.current_location)
                    nearby_location_names = [location.name for location, distance in nearby_location_distances]
                    nearby_locations = [location for location, distance in nearby_location_distances]
                    target_location_name = prompt.split("go to ")[1]
                    if target_location_name in nearby_location_names:
                        if target_location_name == character.current_location.name:
                            print_and_say(f"You are already in {target_location_name}")
                        else:
                            vehicle_names = [vehicle.name for vehicle in character.current_location.vehicles]
                            say(f"please select vehicles to use from {vehicle_names}")
                            while vehicle_name := input(f"please select vehicles to use from {vehicle_names}>>"):
                                if vehicle_name in vehicle_names:
                                    print_and_say(
                                        f"You take {vehicle_name} to {target_location_name}. Have a good travel!")
                                    vehicle = get_object_by_name(vehicle_name, character.current_location.vehicles)
                                    character.current_location.vehicles.remove(vehicle)
                                    print_and_say(f"traveling....")
                                    time.sleep(2)
                                    target_location = get_object_by_name(target_location_name, nearby_locations)
                                    travel_distance = get_location_distance(target_location, nearby_location_distances)
                                    if is_mysterybox_mode:
                                        health_deduction, money_deduction, happiness_deduction, hunger_deduction \
                                            = vehicle.consume_properties(travel_distance)
                                        character.health -= int(health_deduction)
                                        print_and_say(f"You lose {int(health_deduction)} health during travel.")
                                        character.money -= int(money_deduction)
                                        print_and_say(f"You lose {int(money_deduction)} money during travel.")
                                        character.happiness -= int(happiness_deduction)
                                        print_and_say(f"You lose {int(happiness_deduction)} happiness during travel.")
                                        character.hunger -= int(hunger_deduction)
                                        print_and_say(f"You lose {int(hunger_deduction)} hunger during travel.")
                                        check_quest_condition(character)
                                    print_and_say(f"You achieve at {target_location_name}.")
                                    if vehicle not in target_location.vehicles:
                                        target_location.vehicles.append(vehicle)
                                    character.current_location = target_location
                                    break
                                else:
                                    print_and_say(f"There is no such vehicle in {character.current_location.name}")
                                    say(f"please select vehicles to use from {vehicle_names}")
                    else:
                        print_and_say("There is no such location or You cannot direct achieve that location.")

                # TODO: Add dialogue interaction not only single direction
                elif prompt.startswith("talk to"):
                    print_and_say("This function is under redeveloping!")
                    # location_characters = get_characters_by_location(character.current_location)
                    # if character.name in location_characters:
                    #     location_characters.remove(character.name)
                    # target_character = prompt.split("talk to ")[1]
                    # if target_character in location_characters:
                    #     character_dialogues = str_to_class(target_character)().dialogues
                    #     if len(character_dialogues) > 0:
                    #         dialogue = random.choice(character_dialogues)
                    #         print_and_say(f"{target_character}:{dialogue}")
                    #     else:
                    #         print_and_say(f"{target_character} has nothing to talk!")
                    # elif target_character == character.name:
                    #     print_and_say(f"You cannot talk to yourself!")
                    # else:
                    #     print_and_say(f"There is no {target_character} at {character.current_location}!")

                elif prompt.startswith("do"):
                    location_actions = get_actions_by_location(character.current_location)
                    location_actions_names = [action.name for action in location_actions]
                    target_action_item = prompt.split(" ")
                    if len(target_action_item) == 3:
                        target_action = target_action_item[1]
                        target_item = target_action_item[2]
                    elif len(target_action_item) == 2:
                        target_action = target_action_item[1]
                        target_item = None
                    else:
                        target_action = None
                        target_item = None
                    if target_action is None:
                        print_and_say(f"Your input format is wrong!")
                    elif target_action in location_actions_names:
                        target_action = get_object_by_name(target_action, location_actions)
                        if target_item is not None and target_item not in all_character_items_names:
                            target_item = get_object_by_name(target_item, character.current_location.items)
                            character.conduct(target_action, item=target_item)
                        elif target_item is None:
                            character.conduct(target_action, item=target_item)
                        else:
                            print_and_say("There is no such item in the world!")
                    else:
                        print_and_say(f"You cannot {target_action} at {character.current_location}!")

                elif prompt.startswith("use"):
                    target_items_names = [item.name for item in character.items]
                    target_item = prompt.split(" ")[1]
                    if target_item in target_items_names:
                        target_item = get_object_by_name(target_item, character.items)
                        character.use(target_item)
                    else:
                        print_and_say("There is no such item in you packet!")

                elif prompt.startswith("show characters"):
                    location_characters = get_characters_by_location(character.current_location)
                    if character in location_characters:
                        location_characters.remove(character)
                    if len(location_characters) > 0:
                        location_characters_names = [character.name for character in location_characters]
                        print_and_say(f"You found {location_characters_names} in {character.current_location.name}.")
                    else:
                        print_and_say(f"There is no one at {character.current_location.name}")
                elif prompt.startswith("show actions"):
                    location_actions = get_actions_by_location(character.current_location)
                    if len(location_actions) > 0:
                        location_actions_names = [action.name for action in location_actions]
                        print_and_say(
                            f"You can take actions: {location_actions_names} in {character.current_location.name}.")
                    else:
                        print_and_say(f"There is no action to take at {character.current_location.name}")

                elif prompt.startswith("show locations"):
                    nearby_location_distances = game_map.find_nearby_location(character.current_location)
                    if len(nearby_location_distances) > 0:
                        location_names = [location.name for location, distance in nearby_location_distances]
                        print_and_say(f"You found nearby locations: {location_names}!")
                    else:
                        print_and_say(f"There is no other location!")
                elif prompt.startswith("show map"):
                    game_map.show(character.current_location)
                elif prompt.lower().startswith("where am i"):
                    print_and_say(f"You are in {character.current_location.name}!")
                elif prompt.lower().startswith("who am i"):
                    print_and_say(f"You are {character.name}!")
                elif prompt.lower().startswith("change character"):
                    say(f"Please choose the character from the {character_names}")
                    while new_character_name := input(f"Please choose the character from the {character_names}>>"):
                        if new_character_name not in character_names:
                            print_and_say("There is no such character, please reinput!")
                            say(f"Please choose the character from the {character_names}")
                            continue
                        else:
                            character = get_object_by_name(new_character_name, all_characters)
                            print_and_say(f"You are {character.name} and You are in {character.current_location.name}")
                            break
                elif prompt.lower().startswith("show status"):
                    character.show_status()
                elif prompt.lower().startswith("show items"):
                    character.show_items()
                elif prompt.lower().startswith("show objects"):
                    message = f"You found objects in {character.current_location.name}: " + ", ".join(
                        [item.name for item in character.current_location.items])
                    print_and_say(message)
                elif prompt == "q":
                    print_and_say("Bye!")
                    exit(0)
                else:
                    print_and_say("There is no such prompt, please reinput!")
                if is_mysterybox_mode:
                    check_quest_condition(character)


if __name__ == '__main__':
    start()

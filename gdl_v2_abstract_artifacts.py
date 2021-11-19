from math import sqrt
import os
from draw_map import Graph
from copy import deepcopy
import random


def say(message):
    os.system(f"say {message}")


def print_and_say(message):
    print(message)
    say(message)


class Character(object):
    def __init__(self, character_id, name, sex, age, start_location, hunger=100, health=100, money=100, happiness=100,
                 is_npc=False, items=None, actions=None, dialogues=None):
        if items is None:
            items = []
        if actions is None:
            actions = []
        self.character_id = character_id
        self.name = name
        self.sex = sex
        self.age = age
        self.health = health
        self.hunger = hunger
        self.money = money
        self.current_location = start_location
        self.items = items
        self.actions = actions
        self.happiness = happiness
        self.is_npc = is_npc
        self.hold = None
        self.dialogues = dialogues
        if self.dialogues is not None:
            self.dialogues_locations = [dialogue.location for dialogue in dialogues]

    def obtain(self, item):
        if item in self.items and item.reducible:
            self.items[self.items.index(item)].count += item.count
        else:
            self.items.append(deepcopy(item))
        print_and_say(f"You obtained {item.name}.")

    def set_dialogues(self, dialogues):
        self.dialogues = dialogues
        if self.dialogues is not None:
            self.dialogues_locations = [dialogue.location for dialogue in dialogues]

    def drop(self, item):
        self.items.remove(item)

    def hold_item(self, item, place="left hand"):
        if item.is_holdable:
            self.hold = item
            print_and_say(f"You hold the {item.name} on your {place}")
        else:
            print_and_say(f"You cannot hold the {item.name}")

    def attack(self, character):
        if self.hold is not None:
            print_and_say(f"You used {self.hold.name} to attack the {character.name}")
            character.health += self.hold.affect_health
            character.happiness += self.hold.affect_happiness
        else:
            print_and_say("You cannot attack without weapon!")

    def steal(self, character):
        print_and_say(f"You are stealing {character.name} 's money!")
        if character.money > 0:
            self.money += character.money
            character.money = 0
        else:
            print_and_say(f"{character.name} does not have money!")

    def use(self, item):
        if item in self.items:
            if item.reducible:
                self.items[self.items.index(item)].count -= 1
                if self.items[self.items.index(item)].count == 0:
                    self.drop(item)
                print_and_say(f"You used {item.name}...")
                self.health += item.affect_health
                self.money += item.affect_money
                self.happiness += item.affect_happiness
                self.hunger += item.affect_hunger
                item.show_effect()
            else:
                print_and_say("You cannot use this item!")
        else:
            print_and_say("You do not have this item!")

    def conduct(self, action, item=None):
        if action not in self.actions:
            print_and_say(f"You cannot conduct {action.name}!")
        if self.current_location not in action.locations:
            print_and_say(f"You cannot conduct {action.name} in {self.current_location.name}!")
        if item is None:
            action.show(self.current_location)
        else:
            if item in self.items:
                if item.reducible:
                    self.items[self.items.index(item)].count -= 1
                    if self.items[self.items.index(item)].count == 0:
                        self.drop(item)
                    action.use(item)
                    self.health += item.affect_health
                    self.money += item.affect_money
                    self.happiness += item.affect_happiness
                    item.show_effect()
                elif item.is_fixed_item:
                    action.show_items(item)
                elif item.is_holdable:
                    print_and_say(f"You cannot {action} on {item}!")
            elif item.is_container:
                action.conduct(item)
                if len(item.contains_items) > 0:
                    for sub_item in item.contains_items:
                        self.obtain(sub_item)
                    item.contains_items = []
                else:
                    print_and_say(f"There is no item in the {item.name}.")
            else:
                print_and_say(f"You do not have {item.name}!")

    def __eq__(self, other):
        return self.character_id == other.character_id

    def dialogue_response(self, turn_index):
        if self.current_location not in self.dialogues_locations:
            print_and_say(f"{self.name} cannot talk to you in {self.current_location}")
        else:
            cur_dialogue = [dialogue for dialogue in self.dialogues if dialogue.location == self.current_location][0]
            cur_speaker, cur_sentence = cur_dialogue.get_sentence_by_turn(self, turn_index)
            if self == cur_speaker:
                print_and_say(f"{cur_sentence}")
            else:
                print_and_say(f"It's not {self.name}'s turn to speak!")

    def show_status(self):
        message = self.name + ", " + self.sex + ", " + self.age + " years old, \n" \
                  + "health: " + str(self.health) + "\n" \
                  + "hunger: " + str(self.hunger) + "\n" \
                  + "money: " + str(self.money) + "\n" \
                  + "happiness: " + str(self.happiness) + "\n" \
                  + "actions can take: " + " ".join(list(set([action.name + " in "
                                                              + ", ".join([location.name
                                                                           for location in action.locations])
                                                              + "\n" for action in self.actions]))) \
                  + "items can use: \n" + (" ".join([item.name + f"({str(item.count)})" + ": "
                                                     + item.description + "\n" for item in self.items])
                                           if len(self.items) > 0 else "no items!")
        print(message)

    def show_items(self):
        message = "items can use: \n" + (
            " ".join([item.name + f"({str(item.count)})" + ": " + item.description + "\n" for item in self.items])
            if len(self.items) > 0 else "no items!")
        print(message)


class Item(object):
    def __init__(self, item_id, name, description, count=1, reducible=False, is_fixed_item=False, is_holdable=False,
                 is_container=False,
                 affect_hunger=0,
                 affect_health=0,
                 affect_money=0,
                 affect_happiness=0,
                 contains_items=None):
        self.item_id = item_id
        self.name = name
        self.count = count
        self.description = description
        self.reducible = reducible
        self.affect_hunger = affect_hunger
        self.affect_health = affect_health
        self.affect_money = affect_money
        self.affect_happiness = affect_happiness
        self.is_fixed_item = is_fixed_item
        self.is_holdable = is_holdable
        self.is_container = is_container
        if contains_items is not None:
            num_items = len(contains_items)
            num_selected_items = random.randint(1, num_items)
            self.contains_items = random.choices(contains_items, k=num_selected_items)
        else:
            self.contains_items = contains_items


    def __eq__(self, other):
        return self.item_id == other.item_id

    def show_effect(self):
        def show_status(value):
            if value == 0:
                return "has no effect!"
            elif value > 0:
                return f"will increase {value}!"
            else:
                return f"will decrease {abs(value)}!"

        print_and_say("Your health " + show_status(self.affect_health))
        print_and_say("Your money " + show_status(self.affect_money))
        print_and_say("Your happiness " + show_status(self.affect_happiness))
        print_and_say("Your hunger " + show_status(self.affect_hunger))


class Action(object):
    def __init__(self, action_id, name, locations=None, fixed_items=None,
                 location_result_mapping=None, fixed_item_result_mapping=None):
        if location_result_mapping is None:
            location_result_mapping = {}
            for location in locations:
                location_result_mapping[location.name] = "Nothing happened!"
        if fixed_item_result_mapping is None:
            fixed_item_result_mapping = {}
            if fixed_items is not None:
                for fixed_item in fixed_items:
                    fixed_item_result_mapping[fixed_item.name] = "Nothing happened!"

        self.action_id = action_id
        self.name = name
        self.locations = locations
        self.location_result_mapping = location_result_mapping
        self.fixed_item_result_mapping = fixed_item_result_mapping

    def show(self, location):
        print_and_say(self.location_result_mapping[location.name])

    def use(self, item):
        print_and_say(f"You {self.name} {item}...")
        print_and_say(f"{self.name}ing...")

    def show_items(self, fixed_item):
        print_and_say(self.fixed_item_result_mapping[fixed_item.name])

    def conduct(self, container):
        print_and_say(f"{self.name}ing...{container.name}..")


class Location(object):
    def __init__(self, location_id, name, x, y, items, vehicles, fixed_items=None):
        self.location_id = location_id
        self.name = name
        self.x = x
        self.y = y
        self.items = items
        self.fixed_items = fixed_items
        self.vehicles = vehicles

    def __eq__(self, other):
        return self.location_id == other.location_id


class Path(object):
    def __init__(self, location1, location2):
        self.location1 = location1
        self.location2 = location2

    def get_distance(self):
        return round(sqrt((self.location1.x - self.location2.x) * (self.location1.x - self.location2.x) + (
                self.location1.y - self.location2.y) * (self.location1.y - self.location2.y)), 2)


class Map(object):
    def __init__(self, locations, paths):
        self.locations = locations
        self.paths = paths

    def find_nearby_location(self, location):
        nearby_locations = []
        for path in self.paths:
            if path.location2 == location:
                nearby_locations.append((path.location1, path.get_distance()))
            elif path.location1 == location:
                nearby_locations.append((path.location2, path.get_distance()))
        return nearby_locations

    # def find_path(self, location1, location2):
    #     dist = []
    #     path = []
    #     nearby_locations = self.find_nearby_location(location1)
    #     for location, distance in nearby_locations:
    #         pass

    def show(self, current_location):
        all_location_xs = [location.x for location in self.locations]
        all_location_ys = [location.y for location in self.locations]
        max_x = max(all_location_xs)
        min_x = min(all_location_xs)
        max_y = max(all_location_ys)
        min_y = min(all_location_ys)

        def normalized(d, max_d, min_d):

            return (d - min_d) / (max_d - min_d)

        g = Graph()
        for location in self.locations:
            if location == current_location:
                g.add_node(location.name + "*",
                           pos=[normalized(location.x, max_x, min_x), normalized(location.y, max_y, min_y)])
            else:
                g.add_node(location.name,
                           pos=[normalized(location.x, max_x, min_x), normalized(location.y, max_y, min_y)])

        for index, path in enumerate(self.paths):
            if path.location1 == current_location:
                g.add_edge(path.location1.name + "*", path.location2.name, str(path.get_distance()) + "km")
            elif path.location2 == current_location:
                g.add_edge(path.location1.name, path.location2.name + "*", str(path.get_distance()) + "km")
            else:
                g.add_edge(path.location1.name, path.location2.name, str(path.get_distance()) + "km")
        g.draw()
        print_and_say("The \"*\" represents your current location.")


class Vehicle(object):
    def __init__(self, vehicle_id, name, speed, health_consume_speed=None, money_consume_speed=None,
                 happiness_consume_speed=None, hunger_consume_speed=None):
        self.vehicle_id = vehicle_id
        self.name = name
        self.speed = speed
        self.health_consume_speed = health_consume_speed
        self.money_consume_speed = money_consume_speed
        self.happiness_consume_speed = happiness_consume_speed
        self.hunger_consume_speed = hunger_consume_speed

    def consume_properties(self, distance):
        def consume(speed):
            if speed is None:
                print_and_say(f"The {self.name} does not consume health.")
                total_consume = 0
            else:
                total_consume = distance * speed
            return total_consume

        return consume(self.health_consume_speed), consume(self.money_consume_speed), consume(
            self.happiness_consume_speed), consume(self.hunger_consume_speed)

    def compute_time(self, distance):
        return distance / self.speed * 1.0

    def __eq__(self, other):
        return self.vehicle_id == other.vehicle_id


class Dialogue(object):
    def __init__(self, location, target_character, sentences, first_to_speak=True):
        self.location = location
        self.sentences = sentences
        self.target_character = target_character
        self.first_to_speak = first_to_speak

    def get_sentence_by_turn(self, current_character, turn_index=0):
        if self.first_to_speak:
            if turn_index % 2 == 0:
                return current_character, self.sentences[turn_index]
            else:
                return self.target_character, self.sentences[turn_index]
        else:
            if turn_index % 2 == 0:
                return self.target_character, self.sentences[turn_index]
            else:
                return current_character, self.sentences[turn_index]


# TEST
if __name__ == '__main__':
    pass

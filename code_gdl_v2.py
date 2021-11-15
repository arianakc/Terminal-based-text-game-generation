from gdl_v2_abstract_artifacts import *

# Define items including characters owned items and locations fixed objects such as mystery box
health_drug = Item(1, "health_drug", "It is the drug that makes you healthier.", count=5,
                   reducible=True, affect_health=30)
happy_drug = Item(2, "happy_drug", "It is the drug that makes you happy but harm your health", count=5,
                  reducible=True, affect_health=-10, affect_happiness=30)
apple = Item(3, "apple", "An apple can make you not hungry", count=5,
             reducible=True, affect_hunger=10)
poison_apple = Item(4, "poison_apple", "A poison apple can make you not hungry but harm your health", count=5,
                    reducible=True, affect_hunger=10, affect_health=-10)
gold_coin = Item(5, "gold_coin", "These are several gold coins to increase your money by 30", count=2, reducible=True,
                 affect_money=30)
silver_coin = Item(6, "silver_coin", "These are silver gold coins to increase your money by 20", count=2,
                   reducible=True,
                   affect_money=20)
bronze_coin = Item(7, "bronze_coin", "These are bronze gold coins to increase your money by 10", count=2,
                   reducible=True,
                   affect_money=10)
cake = Item(8, "cake", "It is a cake that makes you not hungry.", count=1, reducible=True, affect_hunger=20)
biscuit = Item(9, "biscuit", "It is a biscuit that makes you not hungry.", count=1, reducible=True, affect_hunger=10)


all_character_items = [health_drug, happy_drug, apple, poison_apple, gold_coin, silver_coin, bronze_coin, cake, biscuit]
all_character_items_names = [all_character_item.name for all_character_item in all_character_items]
mystery_box_1 = Item(8, "mystery_box", "A mystery box.", is_container=True,
                     contains_items=[health_drug, gold_coin, apple])
mystery_box_2 = Item(9, "mystery_box", "A mystery box.", is_container=True,
                     contains_items=[happy_drug, poison_apple, bronze_coin])
mystery_box_3 = Item(10, "mystery_box", "A mystery box.", is_container=True,
                     contains_items=[apple, gold_coin])
mystery_box_4 = Item(11, "mystery_box", "A mystery box.", is_container=True,
                     contains_items=[health_drug, happy_drug])
mystery_box_5 = Item(12, "mystery_box", "A mystery box.", is_container=True,
                     contains_items=[silver_coin, apple])
mystery_box_6 = Item(13, "mystery_box", "A mystery box.", is_container=True,
                     contains_items=[poison_apple, bronze_coin])
mystery_box_7 = Item(14, "mystery_box", "A mystery box.", is_container=True,
                     contains_items=[happy_drug, poison_apple])
mystery_box_8 = Item(15, "mystery_box", "A mystery box.", is_container=True,
                     contains_items=[apple, silver_coin, poison_apple])
mystery_box_9 = Item(16, "mystery_box", "A mystery box.", is_container=True,
                     contains_items=[silver_coin, bronze_coin, gold_coin])


# Selected vehicles: bike, plane, train, car
# Define vehicles # speed: km/h health_speed  num/km
bike = Vehicle(vehicle_id=1, name="bike", speed=15, health_consume_speed=1, money_consume_speed=0,
               happiness_consume_speed=1, hunger_consume_speed=1)
plane = Vehicle(vehicle_id=2, name="plane", speed=460, health_consume_speed=0.1, money_consume_speed=1,
                happiness_consume_speed=0, hunger_consume_speed=0)
train = Vehicle(vehicle_id=3, name="train", speed=200, health_consume_speed=0.1, money_consume_speed=0.5,
                happiness_consume_speed=0, hunger_consume_speed=0)
car = Vehicle(vehicle_id=4, name="car", speed=50, health_consume_speed=0.4, money_consume_speed=0.2,
              happiness_consume_speed=0.1, hunger_consume_speed=0.1)
ambulance = Vehicle(vehicle_id=5, name="ambulance", speed=50, health_consume_speed=0.1, money_consume_speed=2,
                    happiness_consume_speed=0, hunger_consume_speed=0)


# Define locations
# Selected Locations: restaurant, house, clinic, airport, hotel, beach, station
# x and y: km
house = Location(location_id=0, name="house", x=0, y=0, items=[mystery_box_1, biscuit], vehicles=[car, bike])
station_1 = Location(location_id=1, name="station_1", x=50, y=30, items=[mystery_box_2], vehicles=[car, bike, train])
airport_1 = Location(location_id=7, name="airport_1", x=50, y=-20, items=[mystery_box_4], vehicles=[car, plane, bike])


station_2 = Location(location_id=2, name="station_2", x=300, y=75, items=[mystery_box_3], vehicles=[car, bike, train])
restaurant = Location(location_id=8, name="restaurant", x=300, y=0, items=[mystery_box_6, cake], vehicles=[car, bike])
clinic = Location(location_id=6, name="clinic", x=300, y=-30, items=[mystery_box_8], vehicles=[car, bike])


airport_2 = Location(location_id=5, name="airport_2", x=540, y=100, items=[mystery_box_5], vehicles=[car, plane, bike])
beach = Location(location_id=4, name="beach", x=600, y=0, items=[mystery_box_7], vehicles=[bike, car])
hotel = Location(location_id=3, name="hotel", x=540, y=-40, items=[mystery_box_9], vehicles=[car, bike])

all_locations = [house, station_1, airport_1, station_2, airport_2, restaurant, clinic, beach, hotel]

# Define paths
paths = [Path(house, station_1), Path(house, airport_1), Path(station_1, airport_1), Path(station_1, station_2),
         Path(station_2, restaurant), Path(restaurant, clinic), Path(airport_1, restaurant), Path(airport_1, clinic),
         Path(airport_1, airport_2), Path(airport_2, beach), Path(airport_2, hotel), Path(hotel, beach),
         Path(clinic, airport_2), Path(station_2, airport_2), Path(station_2, hotel), Path(clinic, hotel)]

# Define Game Map
game_map = Map(locations=all_locations, paths=paths)


# Define characters
# Selected Player Characters: Anna, Marcie, Stanley, Ashley, Kensey, Jackie
# Selected NPCs: Ivy, Jase, Sonya, Bill, John, David, Jason, Mark, Mary
# NEEDS TO DEFINE ACTIONS AND DIALOGUES LATER


# Define Player Characters
jackie = Character(character_id=6, name="Jackie", sex="male", age="26", start_location=house)
anna = Character(character_id=1, name="Anna", sex="female", age="23", start_location=beach)
marcie = Character(character_id=2, name="Marcie", sex="female", age="31", start_location=restaurant)
stanley = Character(character_id=3, name="Stanley", sex="male", age="42", start_location=hotel)
kensey = Character(character_id=5, name="Kensey", sex="male", age="32", start_location=clinic)

characters = [jackie, anna, marcie, stanley, kensey]

# Define Non Player Characters(NPCs)
ivy = Character(character_id=7, name="Ivy", sex="female", age="25", is_npc=True, start_location=house)
ashley = Character(character_id=9, name="Ashley", sex="female", age="25", is_npc=True, start_location=station_1)
sonya = Character(character_id=10, name="Sonya", sex="female", age="30", is_npc=True, start_location=airport_1)
jase = Character(character_id=8, name="Jase", sex="male", age="27", is_npc=True, start_location=restaurant)
bill = Character(character_id=11, name="Bill", sex="male", age="30", is_npc=True, start_location=clinic)
john = Character(character_id=12, name="John", sex="male", age="35", is_npc=True, start_location=station_2)
david = Character(character_id=13, name="David", sex="male", age="37", is_npc=True, start_location=airport_2)
jason = Character(character_id=14, name="Jason", sex="male", age="31", is_npc=True, start_location=beach)
mark = Character(character_id=15, name="Mark", sex="male", age="33", is_npc=True, start_location=hotel)

npcs = [ivy, ashley, sonya, jase, bill, john, david, jason, mark]
all_characters = characters + npcs
# Define actions
dance_location = {restaurant.name: f"You are dancing and other people in the {restaurant.name} are cheering!",
                  house.name: f"You are dancing and the people downstairs feel annoying. They will come to you later, "
                              f"stop and run!"}
dance = Action(action_id=1, name="dance", locations=[restaurant, house], location_result_mapping=dance_location)
eat_1 = Action(action_id=2, name="eat", locations=[restaurant])
eat_2 = Action(action_id=3, name="eat", locations=[house])  # only who starts at house can eat at house
sleep_location = {hotel.name: f"you slept at {hotel.name} and feel very comfortable!",
                  house.name: f"Someone was making noisy outside, you did not sleep well!",
                  beach.name: f"You sleep at beach and the sun is very warm!"}
sleep = Action(action_id=4, name="sleep", locations=[hotel, house, beach], location_result_mapping=sleep_location)
open_box = Action(action_id=5, name="open", locations=all_locations)
check_in_location = {airport_1.name, "You checked in! Please go on board!"}
check_in = Action(action_id=6, name="check_in", locations=[airport_1, airport_2], location_result_mapping=check_in_location)

all_actions = [dance, eat_1, eat_2, sleep, open_box, check_in]

# Add actions for specific player characters
jackie.actions = [dance, eat_1, eat_2, open_box, sleep, check_in]
anna.actions = [dance, eat_1, open_box, sleep, check_in]
marcie.actions = [dance, eat_1, open_box, sleep, check_in]
stanley.actions = [dance, eat_1, open_box, sleep, check_in]
kensey.actions = [dance, eat_1, open_box, sleep, check_in]


# Define dialogues(between player characters and NPCs)


# Define win condition based on character properties (larger or equal than all of them):
win_money = 200
win_hunger = 50
win_happiness = 200
win_health = 1

# Define lose condition based on character properties (no smaller or equal than either one of them):
lose_health = 0
lose_hunger = 0
lose_money = 0
lose_happiness = 0




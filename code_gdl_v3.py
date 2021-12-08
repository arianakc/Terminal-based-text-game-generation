from gdl_v2_abstract_artifacts import *

# source story: https://blog.reedsy.com/short-story/pl21g1/
# Define location
car = Vehicle(vehicle_id=0, name="car", speed=50)
station_office = Location(location_id=0, x=0, y=0, name="station_office", items=[], vehicles=[])
station_walk = Location(location_id=1, x=0.01, y=0.01, name="station_walk", items=[], vehicles=[car])
platform = Location(location_id=2, x=100, y=100, name="platform", items=[], vehicles=[])
building = Location(location_id=1, x=101, y=101, name="building", items=[], vehicles=[])
all_locations = [station_office, station_walk, platform, building]
paths = [Path(station_office, station_walk), Path(station_walk, platform), Path(platform, building)]
game_map = Map(locations=all_locations, paths=paths)
# Define player characters

joseph = Character(character_id=0, name="Joseph", age="22", sex="boy", start_location=station_office, voice="Alex")

characters = [joseph]

all_actions = []
# Define NPCs
angie = Character(character_id=1, name="Angie", age="25", sex="girl", start_location=station_office, voice="Ava")
felix = Character(character_id=2, name="Felix", age="25", sex="boy", start_location=station_walk, voice="Tom")
girl_1 = Character(character_id=3, name="a_girl", age="NA", sex="girl", start_location=station_walk, voice="Ava")
all_characters = [joseph, angie, felix, girl_1]
# Define Dialogue
dialogue_1_sentences = ["You should have just let her jump the gate", "That’s against the rules"]
dialogue_1 = Dialogue(event_id=0, location=station_office, player=joseph, npc=angie, sentences=dialogue_1_sentences,
                      first_to_speak=False)
joseph.dialogues = [dialogue_1]

# Define Event
event_1 = Event(event_id=1,
                instruction="Talk to your coworker Angie.",
                dialogue=dialogue_1,
                end_text="That’s how all your fellow train station managers feel. "
                         "If a customer’s solution is too complicated, "
                         "your coworkers let them go through the emergency exit gate. "
                         "She shrugged in response.",
                characters=[joseph, angie],
                location=station_office)
assist = Action(action_id=0, name="assist", locations=[station_office],
                location_result_mapping={station_office.name: "You assisted the customer."})
joseph.actions.append(assist)
all_actions.append(assist)
event_2 = Event(event_id=2, instruction="You heard a tap on the glass and turned to find a confused-looking customer, "
                                        "card in hand. "
                                        "Please assist them.",
                action=assist, characters=[joseph], location=station_office)
write = Action(action_id=1, name="write", locations=[station_office],
               location_result_mapping={
                   station_office.name: "You wrote “DO NOT TAP ON THE GLASS PLEASE” on a sticky note."})
all_actions.append(write)
joseph.actions.append(write)
event_3 = Event(event_id=3, instruction="You hate when they tap on the glass as if You’m a fish in an aquarium. "
                                        "Please write “DO NOT TAP ON THE GLASS PLEASE” on a sticky note.",
                action=write, characters=[joseph], location=station_office)
tape = Action(action_id=2, name="tape", locations=[station_office],
              location_result_mapping={station_office.name: "You taped the sticky note to the glass."})
all_actions.append(tape)
joseph.actions.append(tape)
event_4 = Event(event_id=4, instruction="Please tape the sticky note to the glass.",
                action=tape, characters=[joseph], location=station_office)
event_3.add_child(event_4)
event_2.add_child(event_3)

dialogue_2_sentences = ["So, first night-shift. You nervous?", "No, why would I be?",
                        "You don’t know, You just seem like the nervous type."]
dialogue_2 = Dialogue(event_id=5, location=station_office, player=joseph, npc=angie, sentences=dialogue_2_sentences,
                      first_to_speak=False)
event_5 = Event(event_id=5, instruction="Talk to your coworker Angie again.", dialogue=dialogue_2,
                end_text="Even though You had been a station manager for over a month, you were nervous. "
                         "You know what to expect for the day shifts, "
                         "and your coworkers make it seem like the night shifts are a whole other world. ",
                characters=[joseph, angie],
                location=station_office)
event_1.add_child(event_5)

dialogue_3_sentences = ["It’s pretty much the same as the day shift, "
                        "People won’t have enough money on the card, "
                        "they don’t know which platform to get on, "
                        "they missed their train and blame you. Ya know, the usual.",
                        "Okay, that sounds easy enough.",
                        "Oh, and another thing, Every once in a while, there’s a bunch of kids who come late at night. "
                        "Never have cards, always jump the gate, and it’s almost always after the last train."]
dialogue_3 = Dialogue(event_id=6, location=station_office, player=joseph, npc=angie, sentences=dialogue_3_sentences,
                      first_to_speak=False)
event_6 = Event(event_id=6, instruction="A few hours went by until You finally got the courage to ask "
                                        "Angie what the night shift was like. "
                                        "You asked as nonchalantly as You could, "
                                        "but she still gave you a smug look in response. "
                                        "Talk to Angie.", dialogue=dialogue_3,
                characters=[joseph, angie],
                location=station_office)

event_7 = Event(event_id=7, instruction="You’d had an uneventful night by the time midnight rolled around. "
                                        "Angie was right, it was more or less the same as the day shifts. "
                                        "You tidied up your side of the station, "
                                        "packed up your bag, and walked out the door. Go to the location station walk.",
                target_location=station_walk, characters=[joseph], location=station_walk)

dialogue_4_sentences = ["Hey! The station is closed. You missed the last train.", "Oh, did I?",
                        "You need to leave, I’m locking up!"]
dialogue_4 = Dialogue(event_id=8, location=station_walk, player=joseph, npc=felix, sentences=dialogue_4_sentences,
                      first_to_speak=True)
event_8 = Event(event_id=8, instruction="As your were fumbling with your keys, "
                                        "you saw a red flash out of the corner of your eye. "
                                        "You turned to see a tall man with blonde hair in a red flannel "
                                        "walk toward the gate and jump over with ease. "
                                        "Talk to the man named Felix.", dialogue=dialogue_4,
                end_text="You set down your bag and walked purposefully to the platform. "
                         "When You reached the escalator, You saw the blonde-haired man in a group of other people. "
                         "You frowned to yourself as You hadn’t noticed anyone else jump the gate. "
                         "That’s it, no more gate-jumping on your watch. ",
                characters=[joseph, felix],
                location=station_walk)

dialogue_5_sentences = ["Excuse me, Excuse me! I am closing the station now, so you all have to leave. "
                        "You shouldn’t even be on the platform anyways if you didn’t scan your card, "
                        "but I’m willing to forget that if you will respectfully "
                        "leave without me having to ask again, "
                        "What’s so funny?",
                        "What makes you think we missed our train?", "Because the last train. It already left–,"]
dialogue_5 = Dialogue(event_id=9, location=station_walk, player=joseph, npc=girl_1, sentences=dialogue_5_sentences,
                      first_to_speak=True)
event_9 = Event(event_id=9, instruction="Talked to the a_girl.", dialogue=dialogue_5, characters=[joseph, girl_1],
                end_text="You raised your wrist to check your watch when you heard the faint sound of a train whistle. "
                         "You looked up at the group who all wore knowing grins. ",
                location=station_walk)

dialogue_6_sentences = ["Sorry, what was that you were saying? You should join us.",
                        "Absolutely not! And neither should any of you! "
                        "This is an unauthorized train. I must report this to my manager"]
dialogue_6 = Dialogue(event_id=10, location=station_walk, player=joseph, npc=felix, sentences=dialogue_6_sentences,
                      first_to_speak=False)
event_10 = Event(event_id=10, instruction="You turned to your right to look down the tracks. "
                                          "Shockingly, You saw the lights of a train "
                                          "flashing around the bend of the tunnel. "
                                          "A single car made its way to the platform and stopped in front of you. "
                                          "The lights turned on and the doors opened, "
                                          "waiting for passengers to come aboard. "
                                          "The rest of the group got on the train, "
                                          "but the man you originally chased stayed. Talk to the Felix.",
                 end_text="You pulled out your phone to search for your manager’s number. "
                          "You turned to see the entire group, blonde-hair-red-flannel man included, "
                          "smiling in their seats. He looked up from the conversation and locked eyes with you. "
                          "You couldn’t look away, so You stared back, and he raised his eyebrows in response. "
                          "You both know what you’re about to do, his expression read. "
                          "The alarm signaled that the doors would close any second. ",
                 dialogue=dialogue_6, characters=[joseph, felix], location=station_walk)

event_9.add_child(event_10)
event_8.add_child(event_9)
event_7.add_child(event_8)

jog_through = Action(action_id=3, name="jog_through", locations=[station_walk],
                     location_result_mapping={station_walk.name: "You jogged through the car doors and "
                                                                 "they immediately shut behind you and "
                                                                 "you realized there was no turning back."})
all_actions.append(jog_through)
joseph.actions.append(jog_through)
event_11 = Event(event_id=11,
                 instruction="You only had a moment to think about it before You decided to jog through the car doors. "
                             "Jump into the car.",
                 characters=[joseph], location=station_walk, action=jog_through)
dialogue_7_sentences = ["What’s your name?", "Joseph", "The name is Felix. Welcome aboard,These are my friends."]

dialogue_7 = Dialogue(event_id=12, location=car, player=joseph, npc=felix,
                      sentences=dialogue_7_sentences, first_to_speak=False)
event_12 = Event(event_id=12, instruction="The group is just as shocked as you are by your presence in the car, "
                                          "except for the blonde-hair-red-flannel man, who looks at you with a huge "
                                          "grin on his face and seems completely amused by the entire situation. "
                                          "He doesn’t break eye contact with you "
                                          "and you feel your cheeks start to turn pink. Talk to Felix.",
                 dialogue=dialogue_7,
                 characters=[joseph, felix], location=station_walk)

dialogue_8_sentences = ["What is all this?", "People’s lives", "Where did you all say this train was going?",
                        "Wherever the last train takes us,"]
dialogue_8 = Dialogue(event_id=13, location=station_walk, player=joseph, npc=felix, sentences=dialogue_8_sentences,
                      first_to_speak=True)
event_13 = Event(event_id=13,
                 instruction="They all smiled at me, still obviously unsure how to feel about you being here. "
                             "As Felix gestured to his friends, You noticed the handprints everywhere, "
                             "all in different shades of gray. "
                             "They blended into each other so well it looked like the car was painted in grayscale. "
                             "There was scribbling on each hand: Accountant, Politician, Janitor, Teacher, Gardener, "
                             "Cashier; the list went on. Talk to Felix.",
                 dialogue=dialogue_8,
                 characters=[joseph, felix], location=station_walk)
event_12.add_child(event_13)
event_11.add_child(event_12)

dialogue_9_sentences = ["Tell me, Joseph, are you going to report us?",
                        "How can I not, Felix? You didn’t swipe your card. "
                        "You took an unauthorized train to an abandoned platform. "
                        "And to make matters worse, you are somehow involved in-in… whatever all this is!",
                        "And You suppose if you don’t report us, you’ll get in trouble and you don’t want that.",
                        "Well of course I don’t! I need this job, I actually care-.",
                        "Cut it out, Joseph, and be real with me. Clearly you don’t care enough about the job. "
                        "Otherwise, you wouldn’t have followed one guy to the aforementioned "
                        "abandoned platform just to threaten a report."]
dialogue_9 = Dialogue(event_id=14, location=station_walk, player=joseph, npc=felix, sentences=dialogue_9_sentences,
                      first_to_speak=False)
event_14 = Event(event_id=14, location=station_walk,
                 instruction="As you walked up the stairs after the train dropped us off, "
                             "You noticed the same pattern of handprints on "
                             "the walls that decorated the train car walls. "
                             "Except, these were much more colorful. Written on them was Painter, Poet, Writer, "
                             "Journalist, Mother, Friend, Scientist, and more. You reached the top of the stairs "
                             "where “welcome to the abandoned platform” was written in black paint on the floor. "
                             "Soft yellow light painted the walls of the underground platform. "
                             "Couches and tables were scattered, each occupied by several people deep in conversation. "
                             "Mesmerized, You made your way through the crowd, and overheard conversation about books "
                             "You’ve never read, movies You’ve never watched, and people You’ve never heard of. "
                             "When you reached the edge of the platform, You peered down to where the tracks "
                             "should have been to see different types of artists creating and selling their work. "
                             "It was as if this underground world was different from the one above. "
                             "Felix walked to a bench in the corner and sat with his legs crossed. "
                             "You hesitated before You walked closer to him. Talk to Felix.",
                 dialogue=dialogue_9,
                 end_text="What was he implying that You wanted to follow him down here, "
                          "as if You had nothing better to do? ",
                 characters=[felix, joseph])

dialogue_10_sentences = ["So, Joseph, what is it that you do?", "Uh, I’m a station manager.",
                         "No, no. What is it you do? When you go home after managing the station.",
                         "I mean, I watch TV and make dinner before I go to bed",
                         "Alright, let’s try this again, "
                         "What is it you used to do but no longer do because you had to become a station manager?",
                         "I used to make maps for fiction books when I was growing up. "
                         "But there’s nothing wrong with being a station manager",
                         "Hey now, You never said there was. "
                         "It’s an important job to keep good people away from troublemakers like me. "
                         "What is wrong is giving up on what gives you life which is why I started The Abandoned.",
                         "Wait, what?",
                         "The Abandoned."
                         " Where you are presently,I found that too many people, even young people, "
                         "have given up on what they love doing on some level. "
                         "I wanted to give people a space to rediscover that love without the pressure of up there. "
                         "I wanted to help people fall in love with life again. It’s nothing really, "
                         "Just some tables and chairs, and people of course. "
                         "I suppose you could do this anywhere, but I liked the metaphor. "
                         "Ya know, these walls are pretty bare, don’t you think?"]
dialogue_10 = Dialogue(event_id=15, location=station_walk, player=joseph, npc=felix,
                       sentences=dialogue_10_sentences, first_to_speak=False)
event_15 = Event(event_id=15, location=station_walk,
                 instruction="While you were lost in that train of thought, another man, not much older than us, "
                             "walked up to Felix. He told him he looked good, that the blonde hair suited him. "
                             "You couldn’t help but agree. Felix was somewhat attractive. He was tall and lean, "
                             "he had a sharp jawline, and a permanent smirk that added a level of confidence "
                             "that could easily draw people in. What people, You're not sure. You're just noting "
                             "his appearance for the report you must write later. "
                             "As you were taking mental pictures (for the report), "
                             "you realized Felix was giving this other man nothing to work with. "
                             "Funnily enough, Felix was staring right at you, ignoring the man’s advances. "
                             "You looked at the ground out of awkwardness and waited until the man left. "
                             "He did eventually, and you could see Felix’s face return to normal. "
                             "Admittedly, it was a better look on him. Talk to Felix.",
                 dialogue=dialogue_10,
                 end_text="He winked at you. You weren't sure what he meant, but then it clicked. "
                          "You smiled at him, sat at the nearest table with a sketchbook, and started working again. "
                          "Felix didn't have to keep your company, but you're glad he did.",
                 characters=[joseph, felix])
event_14.add_child(event_15)

event_16 = Event(event_id=16, instruction="Continue to take car to the final destination platform.",
                 target_location=platform, characters=[joseph, felix, girl_1], location=station_walk)

dialogue_11_sentences = ["Trust me, I’m not as exciting in my normal life", "I find that very hard to believe",
                         "Actually, There is one place. Follow me."]
dialogue_11 = Dialogue(event_id=17, location=station_walk,
                       sentences=dialogue_11_sentences,
                       first_to_speak=True, player=joseph, npc=felix)
event_17 = Event(event_id=17, location=station_walk,
                 instruction="It didn’t take you very long to finish the map. "
                             "For not having done so in who knows how long, "
                             "it didn’t look half bad. You turned it around to show Felix, "
                             "and You couldn’t help notice how handsome he looks when he’s proud of someone, "
                             "when he’s proud of you.  "
                             "You must’ve talked for hours. "
                             "Other people came and went, but you stayed put. "
                             "You liked hearing about other interests and passions. "
                             "You enjoyed sharing your own because of the support and encouragement everyone gave you. "
                             "Felix and You stole glances from each other throughout the night. Talk to Felix.",
                 dialogue=dialogue_11,
                 characters=[joseph, felix])
event_18 = Event(event_id=18, instruction="It didn’t take a lot of convincing. "
                                          "Minutes later you were both above ground, "
                                          "Felix close to your side. There’s a building not far from the platform that "
                                          "You often go to that has the best view in the city. "
                                          "Take walk to the building.",
                 target_location=building, characters=[joseph, felix], location=platform)

dialogue_12_sentences = ["Come over here! Lay down! You took me to the lowest part of the city, "
                         "I took you to the highest",
                         "You call the shots, Joseph. I’ll follow."]
dialogue_12 = Dialogue(event_id=19, player=joseph, npc=felix, sentences=dialogue_12_sentences, location=building)
event_19 = Event(event_id=19,
                 instruction="You make it to the top of the building and "
                             "you see that you only have a few seconds before you miss it. "
                             "He does so with urgency, but You can tell he’s confused. "
                             "A few moments of silence go by and You can feel Felix stare at you. "
                             " He was about to ask what was happening, "
                             "I’m sure, but then You heard the rumble of the plane engine and "
                             "the wind started to pick up. "
                             "Seconds later, the underside of the plane covered your view of the sky almost completely. "
                             "The wind and engine made it impossible to hear Felix’s laugh, "
                             "so you looked over to watch him instead. You’ve seen this before anyways, "
                             "but never his reaction. After the plane passed, "
                             "Felix shot up, still giddy and energized. "
                             "He asked you how you knew that would happen and you shrugged; "
                             "you wanted to keep him interested. Talk to felix.",
                 dialogue=dialogue_12,
                 end_text="He smiled and sat back down in front of you, your toes touching. "
                          "He asked you where you’d take him next so You asked him where he’d like to go.",
                 characters=[joseph, felix], location=building)
event_18.add_child(event_19)
event_17.add_child(event_18)
event_16.add_child(event_17)

event_20 = Event(event_id=20, instruction="You stayed on the roof for a while longer "
                                          "before you made your way back to the platform. "
                                          "Walk back to the platform.",
                 target_location=platform, characters=[joseph, felix], location=building)

event_21 = Event(event_id=21, instruction="The rest of the group was standing in front of the car you took, "
                                          "looking exhausted. You offered to drive the car back and, "
                                          "unsurprisingly, no one objected. Without saying anything, "
                                          "Felix joined you in the driver’s room. "
                                          "You covered all of the basics: school, family, friends, "
                                          "and other things like that. He hung onto yours every word. "
                                          "It felt nice, really nice. Your cheeks hurt from smiling "
                                          "and laughing by the time you pulled back into the station "
                                          "where you came from. Take the car back to the station walk.",
                 target_location=station_walk, characters=[joseph, felix], location=platform)

dialogue_13 = Dialogue(event_id=22, sentences=["I hope I haven’t gotten you fired, "
                                               "because now I have an in with the station managers",
                                               "Was that the only reason for tonight?",
                                               "I’m kidding, I’m kidding, I’m sorry, "
                                               "I just get nervous when… you know what?"], player=joseph, npc=felix,
                       first_to_speak=False, location=station_walk)
event_22 = Event(event_id=22, instruction="You grabbed your bag from the station and locked up behind you. "
                                          "You walked up to the ground level where the group was waiting for you. "
                                          "“When can I see you all again?” You asked.  They smiled and told you soon. "
                                          "Then they waved at you and walked off. Felix stayed behind. "
                                          "His head was hung low and his hands were in his pockets. "
                                          "You hadn’t seen him look so nervous all night. Talk to Felix.",
                 dialogue=dialogue_13, location=station_walk, characters=[joseph, felix],
                 end_text="Felix walked over to you, gently put his hands on either side of your face, "
                          "and kissed you. Sweet and warm, soft and firm. "
                          "He knew what he wanted, and what he wanted was you. "
                          "You kissed him back because you knew you wanted him as well. "
                 )
event_21.add_child(event_22)
event_20.add_child(event_21)

dialogue_14 = Dialogue(event_id=23, sentences=["Hey there, sorry about that, "
                                               "it’s just been so long since I’ve used one of these things. "
                                               "I’ve forgotten how they work.", "You just tap it.",
                                               "Oh well, there’s nowhere important I need to be, anyways. Not anymore,"],
                       location=station_office, player=joseph, npc=felix)
event_23 = Event(event_id=23,
                 instruction="A few days went by and you still hadn’t seen Felix or anyone else from The Abandoned. "
                             "That’s okay, you told yourself. you picked up some extra shifts at the station. "
                             "Not because you wanted to up your chances of seeing Felix, "
                             "but because a little extra money never hurt.  "
                             "you helped as many customers as you could before you let them jump the gate. "
                             "Sometimes it just wasn’t worth the hassle, "
                             "and you're sure these people had somewhere important to be. "
                             "You didn’t want to be the cause of their tardiness. "
                             "You were riding this train of thought when You heard a tap on the glass. "
                             "Someone had taken the post-it note down, "
                             "and you was going to write a new one right after you helped the customer. "
                             "The customer was Felix. He stood there, card in hand, "
                             "and a look of confusion on his face. Talk to Felix",
                 dialogue=dialogue_14,
                 end_text="He nodded his head toward the exit, "
                          "asking you to come with him on his newest great adventure. "
                          "Or maybe just a walk around the block to get coffee. "
                          "Either way, you couldn’t say no. you walked with him, "
                          "hand-in-hand, and didn’t even look back when Angie started banging on the glass. "
                          "you had somewhere more important you needed to be anyway.",
                 characters=[joseph, felix], location=station_office)
# Define scenes
scene_1 = Scene(scene_id=0, events=[event_1, event_2])
scene_2 = Scene(scene_id=1, events=[event_6])
scene_3 = Scene(scene_id=2, events=[event_7])
scene_4 = Scene(scene_id=3, events=[event_11])
scene_5 = Scene(scene_id=4, events=[event_14])
scene_6 = Scene(scene_id=5, events=[event_16])
scene_7 = Scene(scene_id=6, events=[event_20])
scene_8 = Scene(scene_id=7, events=[event_23], refresh_location=True)
scenes = [scene_1, scene_2, scene_3, scene_4, scene_5, scene_6, scene_7, scene_8]


all_character_items = []
all_character_items_names = [all_character_item.name for all_character_item in all_character_items]


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

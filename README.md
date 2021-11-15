# Terminal-based-text-game-generation
Text based game artifacts extraction and terminal-based interactive fiction game generation from natural language stories.

#### Requirements:

- Python3
- Run it on Mac OS since we included "[say](https://ss64.com/osx/say.html)" command
- Relation & Event Extraction, NER dependcies see instructions from https://github.com/dwadden/dygiepp

#### Version 2 after project phase 2 update:

##### [Version 2]GDL update:

- Add abstract artifacts as abstract classes including (Character, Item, Action, Location, Path, Map, Vehicle, Dialogue)...
- Add more properties of characters such as sex, age, health, money, happiness, etc.
- Generate a map of locations with distances
- Add objects in each locations that you can take actions
- Add Location index x, y to compute distance
- The same action can be able to take in different locations and may have different results.
- Using Items can affect characters properties.
- Taking different vechicle can affect characters properties.
- Add gdl support of interaction dialgues but did not finish generating examples(move to project phase 3)
- Implement the mystery box quest with win and lose conditions

##### [Version 2]More prompts:

- "do \<action\> \<item\>" : conduct an action on an item such as "do open mystery_box".
- "show objects": show objects in the current location.
- "show items": show items that the current selected character have.
- "show status": show information about the current selected character.
- "show map": show current map in terminal as ascii graph
- "show locations": show nearby locations instead of all locations on the map.
- "use \<item\>": use an item to change properties of the current selected character.

##### [Version 2]Runing the generated example of version 2([small video demo](https://youtu.be/AVOeYMYu1So)):

```sh
python3 start_game_v2.py
```

##### [Version 2]Modify content in GDL:

- Use open code_gdl_v2.py and see the examples and comments in it.
- You can also refer to gdl_v2_abstract_artifacts.py to see availble artifacts.

#### Previous version 1 after project phase 1:

##### [Version 1]Running the generated example([small video demo](https://youtu.be/1JL1eHgsARI))

```sh
python3 start_game.py
```

##### [Version 1]Available prompts:

- “go to \<location\>” : travel from one location to another location
- “talk to \<character\>”: talk to another character in the same location with you
- “do \<action\>”: perform an action available in that location and see the outputs
- “show characters”: show the list of characters in the same location with you
- “show locations”: show the locations that you have access to
- “show actions”: show the actions that you can perform in your current location
- “where am i”: show your current location
- “who am i”: show your character name
- “change character”: change to another character available in the game
- “q”: quit the game

##### [Version 1]Add more content in GDL to generate new games

1. Open code_gdl.py or create a new one like code_gdl.py. If you create new one with different name, you need to also change the import name of it in start_game.py.
2. Add new characters in variable "characters", then update two character and location mapping variables "clmapping", "lcmapping".
3. For each added new character,  define a character named class below including its name, start location, current locations and dialogues.
4. Add new locations in variable "locations", then update two character and location mapping variables "clmapping", "lcmapping" to add new character in it. Also add it into locations and actions mapping variables "almapping".
5. Add new actions in "almapping" for locations.
6. For each added new action, define a action named class below including its name, result and at which location.
7. Run start_game.py to test new game.

##### [Version 1]Relation Extraction&NER:

please clone the https://github.com/dwadden/dygiepp and follow their instructions.

#### Project Phase

1. **(Finished)** Extract artifacts from natural language stories and generate the code framework
2. **(Finished)** Add more missing parts such as location maps including direction and distance, more characters properties, mystery box quest!
3. **(Todo)** Add stories lines for characters including interactive dialogues:


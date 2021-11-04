# Terminal-based-text-game-generation
Game artifacts extraction and terminal-based interactive fiction game generation from natural language stories.

#### Running the generated example:

```sh
python3 start_game.py
```

#### Available prompts:
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

#### Add more content in GDL to generate new games
1. Open code_gdl.py or create a new one like code_gdl.py. If you create new one with different name, you need to also change the import name of it in start_game.py.
2. Add new characters in variable "characters", then update two character and location mapping variables "clmapping", "lcmapping".
3. For each added new character,  define a character named class below including its name, start location, current locations and dialogues.
4. Add new locations in variable "locations", then update two character and location mapping variables "clmapping", "lcmapping" to add new character in it.
5. Add new actions in "almapping" for locations.
6. For each added new action, define a action named class below including its name, result and at which location.
7. Run start_game.py to test new game.

#### Relation Extraction&NER:
please clone the https://github.com/dwadden/dygiepp and follow their instructions.

#### Project Phase

1. **(Finished)** Extract artifacts from natural language stories and generate the code framework

2. **(Under development)** Add more missing parts such as interactive dialogues, location maps including direction and distance, more characters properties, etc.

3. **(Todo)** Add stories lines or specific tasks for characters just like a text based GTA.


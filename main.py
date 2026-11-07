#Author KARGOL
#Terminal based game about finding flags

#note: add the f command and a progress saving system with a debug function to reset it and do some other stuff
import json

import Build.functions as functions
import config

functions.artPrint('Seek & Poke','slant','light_grey')
print('Type "h" or "help" for help')

while not config.loopBreak:
    c = input("Terminal > ")
    with open('Build/jsons/commands.json') as f:
        commands = json.load(f)
    doesExist = False
    for command in commands:
        if command['name'] == c:
            doesExist = True
            getattr(functions, command['function'])()
            break
        else:
            try:
                if command['alternative'] == c:
                    doesExist = True
                    getattr(functions, command['function'])()
                    break
            except:
                pass
    if not doesExist:
        print('Command does not exist')
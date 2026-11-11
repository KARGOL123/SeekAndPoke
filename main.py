#Author KARGOL
#Terminal based game about finding flags

#note:finish the second flag and finish the syntax reading thing for functions
import json


import Build.functions as functions
import config

functions.flagSetup()
functions.artPrint('Seek & Poke','slant','light_grey')
print('Type "h" or "help" for help')

while not config.loopBreak:
    c = input("Terminal > ")
    cws = c.split(None)[0]
    syntaxCount = functions.countWords(c) - 1
    with open('Build/jsons/commands.json') as f:
        commands = json.load(f)
    doesExist = False
    for command in commands:
        if command['name'] == cws:
            doesExist = True
            if syntaxCount > 0:
                if functions.syntaxCheck(command,syntaxCount,c) == 'NoSupport':
                    print('This command does not support any syntaxes')
                    break
                elif functions.syntaxCheck(command,syntaxCount,c):
                    syntaxes = c.split(None)
                    syntaxes.pop(0)
                    getattr(functions, command['function'])(syntaxes)
                    break
                else:
                    print("Syntax error")
                    break
            else:
                getattr(functions, command['function'])()
                break
        else:
            try:
                if command['alternative'] == cws:
                    doesExist = True
                    if syntaxCount > 0:
                        if functions.syntaxCheck(command, syntaxCount, c) == 'NoSupport':
                            print('This command does not support any syntaxes')
                            break
                        elif functions.syntaxCheck(command, syntaxCount, c):
                            syntaxes = c.split(None)
                            syntaxes.pop(0)
                            getattr(functions, command['function'])(syntaxes)
                            break
                        else:
                            print("Syntax error")
                            break
                    else:
                        getattr(functions, command['function'])()
                        break
            except:
                pass
    if not doesExist:
        print('Command does not exist')
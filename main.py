#Author KARGOL
#Terminal based game about finding flags

#note: add the f command and a progress saving system with a debug function to reset it and do some other stuff

import Build.functions as functions
import Build.longStrings as longStrings
import os

loopBreak = 'no'
functions.artPrint('Seek & Poke','slant','light_grey')
print('Type "h" or "help" for help')

while loopBreak == 'no':
    command = input("Terminal > ")
    if command == 'intro':
        print(longStrings.introString)
    if command == 'h' or command == 'help':
        print(longStrings.helpString)
    if command == 'exit':
        loopBreak = 'yes'
    if command == 'clear':
        os.system('cls' if os.name == 'nt' else 'clear')
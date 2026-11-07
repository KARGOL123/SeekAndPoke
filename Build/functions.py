import sounddevice as sd
import soundfile as sf
import json
import os
from pyfiglet import Figlet
from termcolor import colored

import Build.longStrings as longStrings
import config

def artPrint(text,font,color):
    f = Figlet(font=font)
    print(colored(f.renderText(text),color))

def playSound(file):
    audio, samplerate = sf.read(file)
    sd.play(audio, samplerate)
    sd.wait()

#command functions

def c_intro():
    print(longStrings.introString)
def c_help():
    print('----------\nCommands:')
    with open('Build/jsons/commands.json') as f:
        commands = json.load(f)
    for command in commands:
        text = ('- "'+command['name']+'" ')
        try:
            text = text+('or "'+command['alternative']+'"')
        except:
            pass
        text = text+(': '+command['description'])
        print(text)
    print('----------')
def c_exit():
    config.loopBreak = True
def c_clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def c_flag():
    flag = input()
    if flag == 'dunkin13zbj':
        with open('Build/jsons/save.json') as f:
            save = json.load(f)
        if not save['flags']['flag1']:
            save['flags']['flag1'] = True
            save['flags']['found'] = save['flags']['found'] + 1
            with open('Build/jsons/save.json', 'w') as f:
                json.dump(save, f, indent=4, sort_keys=True)
            print(str(save['flags']['found'])+'/2')

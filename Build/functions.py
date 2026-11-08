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
        try:
            with open('Build/jsons/flags.json') as f:
                flags = json.load(f)
            for flag in flags:
                if command['unlockFlag'] == flag['name']:
                    if flag['found']:
                        text = text + (': ' + command['secretDescription'])
                        break
                    else:
                        text = text + (': ' + command['description'])
                        break
        except:
            text = text+(': '+command['description'])
        print(text)
    print('----------')
def c_exit():
    config.loopBreak = True
def c_clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def c_flag():
    fl = str(input())
    with open('Build/jsons/flags.json') as f:
        flags = json.load(f)
    flagsFound = 0
    flagsCount = 0
    foundNewFlag = False
    for flag in flags:
        flagsCount = flagsCount + 1
        if flag['key'] == fl:
            if not flag['found']:
                flag['found'] = True
                foundNewFlag = True
                with open('Build/jsons/flags.json','w') as f:
                    json.dump(flags,f,indent=4,sort_keys=True)
        if flag['found']:
            flagsFound = flagsFound + 1
    if foundNewFlag:
        print(str(flagsFound) + "/" + str(flagsCount))
def c_debug():
    d = input("Debug: ")
    if d == 'fe':
        tf = input("T or f: ")
        if tf == 't':
            tf = True
        else:
            tf = False
        with open('Build/jsons/flags.json') as f:
            flags = json.load(f)
        o = input("Which flag: ")
        try:
            o =  int(o)
            flags[o-1]['found'] = tf
            with open('Build/jsons/flags.json', 'w') as f:
                json.dump(flags, f, indent=4, sort_keys=True)
        except:
            if o == 'all':
                for flag in flags:
                    flag['found'] = tf
                with open('Build/jsons/flags.json','w') as f:
                    json.dump(flags,f,indent=4,sort_keys=True)
            else:
                print("Why do you even bother using this command?")
    else:
        print("Why do you even bother using this command?")
def c_prog():
    with open('Build/jsons/flags.json') as f:
        flags = json.load(f)
        flagsFound = 0
        flagsCount = 0
        for flag in flags:
            flagsCount = flagsCount + 1
            if flag['found']:
                flagsFound = flagsFound + 1
        print('You have found',str(flagsFound)+'/'+str(flagsCount),'flags')
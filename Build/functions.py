import sounddevice as sd
import soundfile as sf
import random
import json
import os
from pyfiglet import Figlet
from termcolor import colored
from pathlib import Path
from operator import getitem


import Build.longStrings as longStrings
import config

flagsJson = 'Build/jsons/flags.json'
commandsJson = 'Build/jsons/commands.json'

def artPrint(text,font,color):
    f = Figlet(font=font)
    print(colored(f.renderText(text),color))
def playSound(file):
    audio, samplerate = sf.read(file)
    sd.play(audio, samplerate)
def generateKey(length):
    key = ''
    charL = longStrings.charactersList
    for i in range(length):
        key = key + random.choice(charL)
    return key
def flagSetup():
    with open(flagsJson) as f:
        flags = json.load(f)
    for flag in flags:
        if flag['key'] == '':
            flag['key'] = generateKey(8)
    with open(flagsJson, 'w') as f:
        json.dump(flags, f, indent=4, sort_keys=True)
def countWords(string):
    words = string.split(None)
    wordCount = 0
    for i in words:
        wordCount = wordCount+1
    return wordCount
def syntaxCheck(command,syntaxCount,c):
    try:
        syntaxLayer = command['syntaxes']
    except:
        return 'NoSupport'
    allSyntaxesCorrect = False
    for i in range(syntaxCount):
        correctSyntax = False
        finalSyntax = False
        csc = c.split(None)[i + 1]
        try:
            count = -1
            for syn in syntaxLayer:
                count = count + 1
                if syn == csc:
                    correctSyntax = True
                    finalSyntax = True
                    break
                else:
                    try:
                        syn[csc]
                        correctSyntax = True
                        syntaxLayer = getitem(syntaxLayer, count)
                        syntaxLayer = getitem(syntaxLayer, csc)
                        break
                    except:
                        pass
        except:
            pass
        if correctSyntax:
            if finalSyntax and not i + 1 == syntaxCount:
                break
            elif i + 1 == syntaxCount:
                allSyntaxesCorrect = True
                break
        else:
            break
    return allSyntaxesCorrect

#command functions

def c_intro():
    with open(flagsJson) as f:
        flags = json.load(f)
    print(longStrings.introString,'FLAG1:',flags[0]['key']+'\n----------')
def c_help():
    print('----------\nCommands:')
    with open(commandsJson) as f:
        commands = json.load(f)
    for command in commands:
        text = ('- "'+command['name']+'" ')
        try:
            text = text+('or "'+command['alternative']+'"')
        except:
            pass
        try:
            with open(flagsJson) as f:
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
    os.system('cls')
def c_flag():
    fl = str(input())
    with open(flagsJson) as f:
        flags = json.load(f)
    flagsFound = 0
    flagsCount = 0
    flagFunction = str()
    foundNewFlag = False
    for flag in flags:
        flagsCount = flagsCount + 1
        if flag['key'] == fl:
            if not flag['found']:
                flag['found'] = True
                foundNewFlag = True
                flagFunction = flag['function']
                with open(flagsJson,'w') as f:
                    json.dump(flags,f,indent=4,sort_keys=True)
        if flag['found']:
            flagsFound = flagsFound + 1
    if foundNewFlag:
        exec(flagFunction+'()')
        print(str(flagsFound) + "/" + str(flagsCount))
def c_debug():
    d = input("Debug: ")
    if d == 'fe':
        tf = input("T or f: ")
        if tf == 't':
            tf = True
        else:
            tf = False
        with open(flagsJson) as f:
            flags = json.load(f)
        o = input("Which flag: ")
        try:
            o =  int(o)
            flags[o-1]['found'] = tf
            with open(flagsJson,'w') as f:
                json.dump(flags, f, indent=4, sort_keys=True)
        except:
            if o == 'all':
                for flag in flags:
                    flag['found'] = tf
                with open(flagsJson,'w') as f:
                    json.dump(flags,f,indent=4,sort_keys=True)
            else:
                print("Why do you even bother using this command?")
    elif d == 'f_one':
        f_one()
    else:
        print("Why do you even bother using this command?")
def c_prog():
    with open(flagsJson) as f:
        flags = json.load(f)
        flagsFound = 0
        flagsCount = 0
        for flag in flags:
            flagsCount = flagsCount + 1
            if flag['found']:
                flagsFound = flagsFound + 1
        print('You have found',str(flagsFound)+'/'+str(flagsCount),'flags')
def c_whoami():
    print(os.getlogin())

#flag functions

def f_one():
    Path('C:/users/'+os.getlogin()+'/Desktop/Whoami.txt').write_text(longStrings.whoamiString)
    playSound('Assets/Music/somethinghappend.wav')
    artPrint('A new file appeared on your desktop!', 'small', 'green')
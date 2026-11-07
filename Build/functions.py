import sounddevice as sd
import soundfile as sf
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
    print(longStrings.helpString)
def c_exit():
    config.loopBreak = True
def c_clear():
    os.system('cls' if os.name == 'nt' else 'clear')
def c_flag():
    print("Command not ready yet")
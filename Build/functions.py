import sounddevice as sd
import soundfile as sf
from pyfiglet import Figlet
from termcolor import colored

def artPrint(text,font,color):
    f = Figlet(font=font)
    print(colored(f.renderText(text),color))

def playSound(file):
    audio, samplerate = sf.read(file)
    sd.play(audio, samplerate)
    sd.wait()
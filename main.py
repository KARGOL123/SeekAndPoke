#Author KARGOL
#Not sure what this thing is gonna look like at the end

import sounddevice as sd
import soundfile as sf

audio, samplerate = sf.read('Assets/Music/OpsecMusic.wav')

def HelloWorld(t):
    if t == 'print':
        input('Secret code activated, press enter to proceed')
        print("Welcome to Opsec.")
        sd.play(audio, samplerate)
        sd.wait()
    else:
        print(t)

HelloWorld("print")
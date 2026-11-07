import json

def readData(file):
    with open(file) as f:
        data = json.load(f)
    return data
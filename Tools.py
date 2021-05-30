
import json
import re

def readSettings():
    f = open("Settings.json")
    Settings = json.load(f)
    f.close()
    print("Settings Read")
    return Settings

def updateSettings(key,value):
    Settings = readSettings()
    Settings[key] = value
    print(Settings)
    f = open("Settings.json",'w')
    f.write(json.dumps(Settings))
    print("Settings Updated")

def isEmail(email):
    regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
    if (re.search(regex, email)):
        return True
    else:
        return False

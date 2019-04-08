import json

def openJson():
    with open("croquettesdecarottes.json", "r") as recipe:
        myFile = json.load(recipe)
    print(myFile["title"])
openJson()

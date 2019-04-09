import json
from enum import Enum


def OpenJson(arg):
    with open("recette.json", "r") as recipe:
        myFile = json.load(recipe)
        #if arg == "ingredients":
            #for data in myFile[arg]:


        return myFile[arg]


title = OpenJson("title")
portion = int(OpenJson("portion"))
prepTime = OpenJson("prepTime")
cookTime = OpenJson("cookTime")
totalTime = OpenJson("totalTime")
ingredients = OpenJson("ingredients")
steps = OpenJson("steps")
totalSteps = OpenJson("totalSteps")

class quantityType(Enum):
    UNIT = 0
    G = 1
    ML = 2
    SPOON = 3

for ingredient, qty in ingredients.items():
    #print("qty[0] :", qty[0])
    for diffType in quantityType:
        print("diffType :", diffType)
        print("quantityType." + qty[0].upper())
        if "quantityType." + qty[0].upper() == diffType:
            print("before:", type(qty[0]))
            qty[0] = diffType
            print("after:", type(qty[0]))
    #print(type(qty[0]))



#print(ingredients)
import json

with open('recette.json',) as json_data: # Ouverture du fichier en mode lecture
    recette = json.load(json_data) # On le sauvegarde dans une variable
    # recette["prepTime"] = 100 # On modifie une valeur garce à cette var ( comme un dict)
    title = recette['title']
    portion = recette['portion']
    prepTime = recette['prepTime']
    cookTime = recette['cookTime']
    totalTime = recette['totalTime']

    

with open('recette.json', 'w') as json_data: # On réouvre le fichier mais en écriture
    json.dump(recette, json_data, indent=4) # On met à jour le fichier avec dump

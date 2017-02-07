# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

import os
from roboc.carte import Carte
from roboc.RobocException import RobocException


# On charge les cartes existantes


'''
    Let the player choose his map, load it and play it later
'''
def loadPlayedMap():
    cartes = []
    saves = []
    #localpath= os.getcwd().replace('\\', '/')
    absolutePathToMaps = os.path.abspath("./roboc/cartes")
    absolutePathToSaves = os.path.abspath("./roboc/saves")
    
    for nom_fichier in os.listdir(absolutePathToMaps):
        if nom_fichier.endswith(".txt"):
            path = os.path.join(absolutePathToMaps, nom_fichier)
            name = nom_fichier[:-3].lower()
            cartes.append(Carte(name, path))
    
    print("Labyrinthes existants :")
    for i, carte in enumerate(cartes):
        print("  {} - {}".format(i + 1, carte.nom))
    
    for file in os.listdir(absolutePathToSaves):
        if file.endswith(".txt"):
            path = os.path.join(absolutePathToMaps, nom_fichier)
            name = nom_fichier[:-3].lower()
            saves.append(Carte(name, path))
            
    allMaps = len(cartes)
    for i, carte in enumerate(saves):
        print("  {} - [saved] {}".format(i + len(cartes) + 1, carte.nom))

    select = 0
    allMaps += len(saves)
    while (select < 1 or select > allMaps):
        selectStr = input ("Entrez un numéro de labyrinthe pour commencer à jouer: ")
        try :
            select = int(selectStr)
        except:
            select = 0
    
    if select >= len(cartes):
        mapPlayed = saves[select - len(cartes) -1]
    else :
        mapPlayed = cartes[select -1]

    #We load only when it's sure we'll play this map
    
    
    return mapPlayed




if __name__ == '__main__':
    
    mapPlayed = loadPlayedMap()
    loadOK = False
    while not loadOK:
        try:
            mapPlayed.load()
            loadOK = True
        except RobocException: 
            print ("La carte est corrompue, veuillez en choisir une autre")
            mapPlayed = loadPlayedMap()
    print(mapPlayed.maze)












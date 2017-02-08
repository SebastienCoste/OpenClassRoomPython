# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

from roboc.RobocException import RobocException
from roboc.Ihm import IHM
from roboc.Validator import Validator
from roboc.connector import Messages as m
import argparse
# On charge les cartes existantes





if __name__ == '__main__':
    
    parser = argparse.ArgumentParser()
    parser.parse_args()
    parser.add_argument("-l", "--lan", help="language: 'fr'(default) or 'en'")
    args = parser.parse_args()
    lan = "FR"
    if args.lan:
        if args.lan.upper() in m.authorizedLan:
            lan = args.lan.upper()
        else:
            raise RobocException("Unrecognized language")
    
    
    
    #the manager talks with the player
    manager = IHM(lan)
    
    #The validator of map, moves
    validator = Validator()
    
    #Let's get the map
    mapPlayed = manager.loadPlayedMap()
    loadOK = False
    while not loadOK:
        try:
            mapPlayed.load()
            validator.validateInitMap(mapPlayed)
            loadOK = True
        except RobocException as rex: 
            manager.send("WrongMap")
            manager.send(rex)
            mapPlayed = manager.loadPlayedMap()
    manager.printMaze(mapPlayed)
    
    #Before we play, we save
    if mapPlayed.saveName == None:
        path, name = manager.getSavePathAndName()
        mapPlayed.setSavePath(path, name)
        mapPlayed.save()

    #Now We play
    playerWannaPlay = True
    while not validator.thisIsTheEnd(mapPlayed) and playerWannaPlay:
        move = manager.getNextMove()
        if move == None:
            playerWannaPlay = False
            continue
        
        pass
        
    if validator.thisIsTheEnd(mapPlayed):
        manager.keepOrDelete(mapPlayed)









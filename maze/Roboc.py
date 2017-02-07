# -*-coding:Utf-8 -*

"""Ce fichier contient le code principal du jeu.

Exécutez-le avec Python pour lancer le jeu.

"""

from roboc.RobocException import RobocException
from roboc.Ihm import IHM
from roboc.Validator import Validator
from roboc import Messages as m

# On charge les cartes existantes





if __name__ == '__main__':
    
    #the manager talks with the player
    manager = IHM()
    
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
            manager.send(m.WrongMap + rex)
            mapPlayed = manager.loadPlayedMap()
    manager.send(mapPlayed.maze)
    
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









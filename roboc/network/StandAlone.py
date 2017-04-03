'''
Created on Apr 3, 2017

@author: Static
'''
from roboc.RobocException import RobocException
from roboc.network import NetworkType
from roboc.Ihm import IHM
from roboc.Validator import Validator

class StandAlone:
    
    def __init__(self, lan):
        #the manager talks with the player
        self.manager = IHM(lan, NetworkType.STANDALONE)
        #The validator of map, moves
        self.validator = Validator()
        
    def run(self):
        #Let's get the map
        iWantToPlayAGame = True
        while iWantToPlayAGame:
            mapPlayed = self.manager.loadPlayedMap()
            loadOK = False
            while not loadOK:
                try:
                    mapPlayed.load()
                    self.validator.validateInitMap(mapPlayed)
                    loadOK = True
                except RobocException as rex: 
                    self.manager.send("WrongMap")
                    self.manager.send(rex)
                    mapPlayed = self.manager.loadPlayedMap()
            self.manager.printMaze(mapPlayed)
            
            #Before we play, we save
            if mapPlayed.saveName == None:
                path, name = self.manager.getSavePathAndName()
                mapPlayed.setSavePath(path, name)
                mapPlayed.save()
        
            #Now We play
            playerWannaPlay = True
            while not self.validator.thisIsTheEnd(mapPlayed) and playerWannaPlay:
                move, times = self.manager.getNextMove()
                if move == None:
                    playerWannaPlay = False
                    continue
                timesMove = self.validator.validateMove(mapPlayed, move, times)
                if timesMove == 0 :
                    self.manager.send("WrongMove")
                else:
                    mapPlayed.moveAlong(move, timesMove, self.manager)
                if self.validator.thisIsTheEnd(mapPlayed):
                    continue
                
            if self.validator.thisIsTheEnd(mapPlayed):
                self.manager.keepOrDelete(mapPlayed)
            
            iWantToPlayAGame = self.manager.playAnotherGame()
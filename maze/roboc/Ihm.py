# -*-coding:Utf-8 -*
'''
Created on Feb 7, 2017

@author: Static
'''

import os, re
from roboc.Carte import Map
from roboc.RobocException import RobocException
from roboc.connector import Connector

class IHM:
    '''
    Here we manage interactions with the player
    '''


    def __init__(self, lan):
        self.c = Connector(lan)
        self.absolutePathToMaps = os.path.abspath("./roboc/cartes")
        self.absolutePathToSaves = os.path.abspath("./roboc/saves")
        self.existingNames = []
        self.matcher = re.compile(r"^[A-Za-z0-9]+$")
        self.matcherMove = re.compile(r"^[SsNnOoEe][0-9]{,4}$")
        self.matcherQuit = re.compile(r"^[Qq]$")
        self.matcherYes = re.compile(r"^[OoYy]$")
        self.matcherNo = re.compile(r"^[Nn]$")
        self.matcherYesNo = re.compile(r"^[OoYyNn]$")
    

    '''
        Let the player choose his map, load it and play it later
    '''
    def loadPlayedMap(self):
        cartes = []
        saves = []
        #localpath= os.getcwd().replace('\\', '/')
        
        for file in os.listdir(self.absolutePathToMaps):
            if file.endswith(".txt"):
                path = os.path.join(self.absolutePathToMaps, file)
                name = file[:-3].lower()
                cartes.append(Map(name, path))
        
        self.c.send("ExistingMaze")
        for i, carte in enumerate(cartes):
            self.c.send("  {} - {}".format(i + 1, carte.nom))
        
        for file in os.listdir(self.absolutePathToSaves):
            if file.endswith(".txt"):
                path = os.path.join(self.absolutePathToSaves, file)
                name = file[:-3].lower()
                saves.append(Map(name, path))
                self.existingNames.append(file[:-4])
                
        allMaps = len(cartes)
        for i, carte in enumerate(saves):
            self.c.send("  {} - [saved] {}".format(i + len(cartes) + 1, carte.nom))
    
        select = 0
        allMaps += len(saves)
        while (select < 1 or select > allMaps):
            selectStr = self.c.ask ("GetNumberOfMaze")
            try :
                select = int(selectStr)
            except:
                select = 0
        
        if select >= len(cartes):
            mapPlayed = saves[select - len(cartes) -1]
            mapPlayed.savepath = self.absolutePathToSaves
            mapPlayed.saveName = mapPlayed.nom + "txt"
        else :
            mapPlayed = cartes[select -1]
            mapPlayed.saveName = None
    
        #We load only when it's sure we'll play this map
        return mapPlayed
    
    def getSavePathAndName(self):
        nameFound = ""
        while self.matcher.search(nameFound) is None:
            nameFound = self.c.ask ("GetSavePathAndName")
            nameFound = nameFound.strip()
            if nameFound in self.existingNames:
                nameFound = ""
            
        return self.absolutePathToSaves, nameFound+".txt"
    
    def keepOrDelete(self, mapPlayed):
        answer = ""
        while self.matcherYesNo.search(answer) is None:
            answer = self.c.ask ("KeepOrDelete")
            
        if not self.matcherYes.search(answer) is None:
            os.remove(os.path.join(mapPlayed.savepath, mapPlayed.saveName))
    
    def getNextMove(self):
        answer = ""
        while self.matcherMove.search(answer) is None and self.matcherQuit.search(answer) is None:
            answer = self.c.ask ("GetNextMove")
        if not self.matcherQuit.search(answer) is None:
            return None
        return answer
    
    def send(self, message):
        self.c.send(message)
    
    def printMaze(self, mapPlayed):
        self.c.printMaze(mapPlayed)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
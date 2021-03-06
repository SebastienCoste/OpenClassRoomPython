# -*-coding:Utf-8 -*
'''
Created on Feb 7, 2017

@author: Static
'''

import os, re
from roboc.game.Carte import Map
from roboc.RobocException import RobocException
from roboc.connector.Connector import Connector
from roboc.connector.Translator import Translator

class IHM:
    '''
    Here we manage interactions with the player. 
    Everything is gathered in one class. Let say we want an IA, it replaces this class 
    '''


    def __init__(self, lan, type):
        self.c = Connector(lan, type)
        self.translator = Translator(lan)
        
        if not lan == "FR": 
           self.c.send("LanBeta")   
        self.absolutePathToMaps = os.path.abspath("./roboc/cartes")
        self.absolutePathToSaves = os.path.abspath("./roboc/saves")
        self.existingNames = []
        self.matcher = re.compile(r"^[A-Za-z0-9]+$")
        self.matcherMove = re.compile(r"^[" + self.translator.getTechMatcher("matcherMove") + "][ ]*[0-9]{,4}$")
        self.matcherQuit = re.compile(r"^[" + self.translator.getTechMatcher("matcherQuit") + "]$")
        self.matcherYes = re.compile(r"^[" + self.translator.getTechMatcher("matcherYes") + "]$")
        self.matcherNo = re.compile(r"^[" + self.translator.getTechMatcher("matcherNo") + "]$")
        self.matcherYesNo = re.compile(r"^[" + self.translator.getTechMatcher("matcherYesNo") + "]$")
    

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
                self.c.send("ExistingSave")
                nameFound = ""
            
        return self.absolutePathToSaves, nameFound+".txt"
    
    def playAnotherGame(self):
        answer = ""
        while self.matcherYesNo.search(answer) is None:
            answer = self.c.ask ("PlayAnotherGame")
        return not self.matcherYes.search(answer) is None
    
    
    def keepOrDelete(self, mapPlayed):
        answer = ""
        while self.matcherYesNo.search(answer) is None:
            answer = self.c.ask ("KeepOrDelete")
            
        if not self.matcherYes.search(answer) is None:
            os.remove(os.path.join(mapPlayed.savepath, mapPlayed.saveName))
            os.remove(os.path.join(mapPlayed.savepath, mapPlayed.saveName.replace('txt', 'dat')))
    
    def getNextMove(self):
        answer = ""
        while self.matcherMove.search(answer) is None and self.matcherQuit.search(answer) is None:
            answer = self.c.ask ("GetNextMove")
            answer = answer.replace(' ', '').upper()
        if not self.matcherQuit.search(answer) is None:
            return None, None
        move = self.translator.getMove(answer[:1])
        times = 1
        if len(answer) > 1:
            try :
                times = int(answer[1:])
            except:
                times = 1
        return move, times
    
    def send(self, message):
        self.c.send(message)
    
    def printMaze(self, mapPlayed):
        self.c.printMaze(mapPlayed)
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    


# -*-coding:Latin-1 -*
'''
Created on Feb 7, 2017
If we don't want to talk through sysout, we can change the connector 
@author: Static
'''
from roboc.connector.Translator import Translator

class Connector:
    
    def __init__(self, lan):
        self.lan = lan
        self.translator = Translator(lan)
        
    def ask(self, message):
        return input (self.translator.getMessage(message))
    
    def send(self, message):
        print(self.translator.getMessage(message))
        
    def printMaze(self, mapPlayed):
        res = "";
        for h in mapPlayed.maze.grid:
            res +=''.join(h) + '\n'
        print(res)
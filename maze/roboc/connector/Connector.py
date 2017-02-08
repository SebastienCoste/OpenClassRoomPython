# -*-coding:Latin-1 -*
'''
Created on Feb 7, 2017
If we don't want to talk through sysout, we can change the connector 
@author: Static
'''

class Connector:
    
    def __init__(self, lan):
        self.lan = lan
        
    def ask(self, message):
        return input (message)
    
    def send(self, message):
        print(message)
        
    def printMaze(self, mapPlayed):
        res = "";
        for h in mapPlayed.maze.grid:
            res +=''.join(h) + '\n'
        return res
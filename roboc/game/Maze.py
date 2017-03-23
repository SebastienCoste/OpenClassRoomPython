# -*-coding:Utf-8 -*

"""Ce module contient la classe Maze."""

from roboc.Point import Point
from roboc.RobocException import RobocException
import os

class Maze:
    
    authorisedChars = [' ', 'O', 'X', 'U', '.']
    walkableChars = [' ', 'X', 'U', '.']
    significations= {
    " " : "EMPTY",
    "X" : "ROBOT",
    "U" : "EXIT",
    "." : "DOOR"           
    }

    """Classe représentant un labyrinthe."""

    def __init__(self, dumpString):
        self.grid = [[]]
        height, width = 0,0
        mazewidth = -1
        self.exit = None
        self.robot = None
        for c in dumpString:
            if (c == '\n'):
                if width == 0:
                    continue
                height+=1
                self.grid.append([])
                if mazewidth == -1:
                    mazewidth = width
                if mazewidth != width:
                    raise RobocException("Toutes les lignes doivent etre de la même longueur")
                width = 0
                continue
            elif (c.upper() not in Maze.authorisedChars):
                continue
            else:
                self.grid[height].append(c)
                if (c.upper() == 'X'):
                    self.robot = Point(height, width)
                elif (c.upper() == 'U'):
                    self.exit = Point(height, width)
            
            width +=1

    def isWalkingPoint(self, position):
        return self.grid[position.height][position.width] in Maze.walkableChars
    
    def getValuePoint(self, position):
        return Maze.significations[self.grid[position.height][position.width]]
    
    def moveRobot(self, position, currentPositionType):
        if currentPositionType == "DOOR":
            self.grid[self.robot.height][self.robot.width] = '.'
        else:
            self.grid[self.robot.height][self.robot.width] = ' '
        self.robot = position
        self.grid[self.robot.height][self.robot.width] = 'X'
    
    def __str__(self):
        res = "";
        for h in self.grid:
            res +=''.join(h) + '\n'
        return res
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        

# -*-coding:Utf-8 -*

"""Ce module contient la classe Maze."""

from roboc.Point import Point
from roboc.RobocException import RobocException
class Maze:
    
    authorisedChars = [' ', 'O', 'X', 'U', '.']

    """Classe représentant un labyrinthe."""

    def __init__(self, dumpString):
        self.grille = [[]]
        height, width = 0,0
        mazewidth = -1
        for c in dumpString:
            if (c == '\n'):
                height+=1
                self.grille.append([])
                if mazewidth == -1:
                    mazewidth = width
                if mazewidth != width:
                    raise RobocException("Toutes les lignes doivent etre de la même longueur")
                width = 0
                continue
            elif (c.upper() not in Maze.authorisedChars):
                continue
            else:
                self.grille[height].append(c)
                if (c.upper() == 'X'):
                    self.robot = Point(height, width)
                elif (c.upper() == 'U'):
                    self.exit = Point(height, width)
            
            width +=1

    
    def __str__(self):
        res = "";
        for h in self.grille:
            res +=''.join(h) + '\n'
        return res

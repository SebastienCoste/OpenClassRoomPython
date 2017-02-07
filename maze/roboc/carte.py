# -*-coding:Latin-1 -*
'''
Created on Feb 7, 2017
@author: Static
'''

from roboc.labyrinthe import Maze

class Carte:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, filepath):
        self.nom = nom
        self.filepath = filepath
        self.maze = None #creer_labyrinthe_depuis_chaine(chaine)

    def __repr__(self):
        return "<Carte {}>".format(self.nom)
    
    def load(self):
        with open(self.filepath, 'r') as file:
            dumpString = file.read()
            self.maze = Maze(dumpString)

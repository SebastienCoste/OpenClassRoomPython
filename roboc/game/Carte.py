# -*-coding:Latin-1 -*
'''
Created on Feb 7, 2017
@author: Static
'''

from roboc.game.Maze import Maze
from roboc.game.Data import Data
import os, pickle

class Map:

    """Objet de transition entre un fichier et un labyrinthe."""

    def __init__(self, nom, filepath):
        self.nom = nom
        self.filepath = filepath
        self.maze = None #creer_labyrinthe_depuis_chaine(chaine)
        self.data = None

    def __repr__(self):
        return "<Map {}>".format(self.nom)
    
    def load(self):
        with open(self.filepath, 'r') as file:
            dumpString = file.read()
            self.maze = Maze(dumpString)
        
        with open(self.filepath.replace('txt', 'dat'), 'rb') as file:
            depick = pickle.Unpickler(file)
            self.data = depick.load()
        if self.data == None:
            self.data = Data()
    
    def setSavePath(self, path, name):
        self.savepath = path
        self.saveName = name
        
    def save(self):
        with open(os.path.join(self.savepath, self.saveName), 'w') as file:
            file.write(str(self.maze))
        
        with open(self.filepath.replace('txt', 'dat'), 'wb') as file:
            pick = pickle.Pickler(file)
            pick.dump(self.data)
            
            
            
            
            
# -*-coding:Latin-1 -*
'''
Created on Feb 4, 2017

@author: Static
'''
import os, pickle

inventaire = [
     ("pommes", 22),
     ("melons", 4),
     ("poires", 18),
     ("fraises", 76),
     ("prunes", 51),
]

if __name__ == '__main__':
    os.chdir("../res")
    with open("data", 'wb') as fichier:
        pick = pickle.Pickler(fichier)
        pick.dump(inventaire)
    with open("data", 'rb') as file:
        unpick = pickle.Unpickler(file)
        invent = unpick.load()
        print (invent)
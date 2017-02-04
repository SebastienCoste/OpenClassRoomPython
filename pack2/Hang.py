# -*-coding:Latin-1 -*
'''
Created on Feb 4, 2017

@author: Static
'''
import random as r
import re
import os, pickle
from http.client import FOUND

nbChances = 8
liste_mots = [
    "armoire",
    "boucle",
    "buisson",
    "bureau",
    "chaise",
    "carton",
    "couteau",
    "fichier",
    "garage",
    "glace",
    "journal",
    "kiwi",
    "lampe",
    "liste",
    "montagne",
    "remise",
    "sandale",
    "taxi",
    "vampire",
    "volant",
]
players = {"":(0,0)}

def validate(test):
    if len(test) != 1:
        return False
    return test.isalpha()

if __name__ == '__main__':
    
    os.chdir("../res")
    if not os.path.isfile("hang"):
        with open("hang", 'wb') as file:
            pickler = pickle.Pickler(file)
            pickler.dump(players)
    with open("hang", 'rb') as file:
        unpick = pickle.Unpickler(file)
        players = unpick.load()
    del(players[""])    
    player = input ("player name\n")
    if player in players.keys():
        (wins, losses) = players[player]
    else:
        (wins, losses) = 0, 0
        
    nbrWords = len(liste_mots)
    guessNum = r.randrange(nbrWords)
    guess = liste_mots[guessNum]
    currentGuess = "*"*len(guess)
    tested = "";
    
    print (currentGuess)
    print (guess)
    found = False
    while nbChances>0 and not found:
        letter = input ("guess a letter\n").lower()
        if not validate(letter):
            continue
        lstCurrent = list(currentGuess)
        goodGuess = False
        for i, l in enumerate(guess):
            if l == letter:
                lstCurrent[i] = l
                goodGuess = True
        if not goodGuess:
            tested += letter
            nbChances-=1
        currentGuess = ''.join(lstCurrent)    
        found = not "*" in currentGuess
        print("[{}] - tries:{} on {}".format(currentGuess, 8-nbChances, tested))
    
    if found:
        wins +=1
    else: 
        losses +=1
    
    print("W:{}, L:{}".format(wins, losses))
    players[player] = (wins, losses)
    with open("hang", 'wb') as file:
            pickler = pickle.Pickler(file)
            pickler.dump(players)

    print(players)



















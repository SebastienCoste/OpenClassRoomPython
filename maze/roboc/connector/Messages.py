# -*-coding:Latin-1 -*
'''
Created on Feb 7, 2017
 All managed languages
starting i18n as well
@author: Static
'''

French= {
    "KeepOrDelete": "Partie terminee. Voulez vous supprimer la sauvegarde? O/N",
    "GetNextMove": "Quel est votre prochain mouvement ? N:Nord, S:Sud, O:Ouest, E:Est, Q:Quitter",
    "GetSavePathAndName": "Quel nom donner à la sauvegarde? (caracteres alphanumeriques uniquement)",
    "GetNumberOfMaze": "Entrez un numéro de labyrinthe pour commencer à jouer: ",
    "ExistingMaze": "Labyrinthes existants :",
    "WrongMap": "La carte est corrompue, veuillez en choisir une autre.",
    "UnknownMove": "Lettre non reconnue (S N O E uniquement)",
}

English= {
    "KeepOrDelete": "Game ended. Do you want to delete the save? Y/N",
    "GetNextMove": "What is your next move ? N:North, S:South, W:West, E:Est, Q:Quit",
    "GetSavePathAndName": "How the save will be named? (alphanumeric characters only)",
    "GetNumberOfMaze": "Select the number of the maze you want to play: ",
    "ExistingMaze": "Existing mazes :",
    "WrongMap": "the maze is corrupted, please take another.",
    "UnknownMove": "Unrecognized move (S N O E only)",
}

authorizedLan = ["FR", "EN"]
LanguageToMessages = {authorizedLan[0]: French, authorizedLan[1]: English}
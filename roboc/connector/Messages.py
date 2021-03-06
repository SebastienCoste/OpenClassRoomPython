# -*-coding:Latin-1 -*
'''
Created on Feb 7, 2017
 All managed languages
starting i18n as well
@author: Static
'''

#messages 
French= {
    "KeepOrDelete": "Partie terminee. Voulez vous supprimer la sauvegarde? O/N",
    "PlayAnotherGame" : "Jouer une autre partie ? O/N",
    "GetNextMove": "Quel est votre prochain mouvement ? N:Nord, S:Sud, O:Ouest, E:Est, Q:Quitter",
    "GetSavePathAndName": "Quel nom donner � la sauvegarde? (caracteres alphanumeriques uniquement)",
    "GetNumberOfMaze": "Entrez un num�ro de labyrinthe pour commencer � jouer: ",
    "ExistingMaze": "Labyrinthes existants :",
    "WrongMap": "La carte est corrompue, veuillez en choisir une autre.",
    "UnknownMove": "Lettre non reconnue (S N O E uniquement)",
    "ExistingSave" : "Une sauvegarde portant ce nom existe deja",
    "WrongMove" : "Le deplacement est impossible",
    "LanBeta" : "Attention cette langue est en beta test"
}

English= {
    "KeepOrDelete": "Game ended. Do you want to delete the save? Y/N",
    "PlayAnotherGame" : "Play another game ? Y/N",
    "GetNextMove": "What is your next move ? N:North, S:South, W:West, E:Est, Q:Quit",
    "GetSavePathAndName": "How the save will be named? (alphanumeric characters only)",
    "GetNumberOfMaze": "Select the number of the maze you want to play: ",
    "ExistingMaze": "Existing mazes :",
    "WrongMap": "the maze is corrupted, please take another.",
    "UnknownMove": "Unrecognized move (S N O E only)",
    "ExistingSave": "A save with this name already exists",
    "WrongMove" : "Unable to move along this path",
    "LanBeta" : "Please notice the language is still in beta test"
}

#Technical configuration
FrenchTech= {
    "matcherMove": "SsNnOoEe",
    "matcherQuit": "Qq",
    "matcherYes": "Oo",
    "matcherNo": "Nn",
    "matcherYesNo": "OoNn"
    }       
EnglishTech= {
    "matcherMove": "SsNnOoEe",
    "matcherQuit": "Qq",
    "matcherYes": "Yy",
    "matcherNo": "Nn",
    "matcherYesNo": "YyNn"
    }

FrenchMoves = {
    "N":"UP",
    "S":"DOWN",
    "E":"RIGHT",
    "O":"LEFT"
    }
EnglishMoves = {
    "N":"UP",
    "S":"DOWN",
    "E":"RIGHT",
    "W":"LEFT"
    }

authorizedLan = ["FR", "EN"]
LanguageToMessages = {authorizedLan[0]: French, authorizedLan[1]: English}
LanguageToTech = {authorizedLan[0]: FrenchTech, authorizedLan[1]: EnglishTech}
LanguageToMove = {authorizedLan[0]: FrenchMoves, authorizedLan[1]: EnglishMoves}
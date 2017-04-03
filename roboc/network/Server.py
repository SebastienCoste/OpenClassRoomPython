'''
Created on Apr 3, 2017

@author: Static
'''
from roboc.network import NetworkType
from roboc.Ihm import IHM
from roboc import Validator
class Server:
    
    
    def __init__(self, lan):
        #the manager talks with the player
        self.manager = IHM(lan, NetworkType.SERVER)
        #The validator of map, moves
        self.validator = Validator()
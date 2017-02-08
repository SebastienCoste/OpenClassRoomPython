# -*-coding:Latin-1 -*
'''
Created on Feb 7, 2017
@author: Static
'''

from roboc.RobocException import RobocException

class Validator:
    
    def __init__(self):
        pass

    def validateInitMap(self, map):
        
        if map.maze.robot == None:
            raise RobocException ("No Robot Exception")

    def thisIsTheEnd(self, map):
        return map.maze.robot.equals(map.maze.exit)
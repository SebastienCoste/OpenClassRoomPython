# -*-coding:Latin-1 -*
'''
Created on Feb 7, 2017
@author: Static
'''

from roboc.RobocException import RobocException
from roboc import Messages as m

class Validator:
    
    def __init__(self):
        pass

    def validateInitMap(self, map):
        
        if map.maze.robot == None:
            raise RobocException (m.NoRobot)

    def thisIsTheEnd(self, map):
        return map.maze.robot.equals(map.maze.exit)
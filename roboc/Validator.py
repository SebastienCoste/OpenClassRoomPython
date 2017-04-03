# -*-coding:Latin-1 -*
'''
Created on Feb 7, 2017
@author: Static
'''

from roboc.RobocException import RobocException

'''
    Validation machine. It validate the map at start 
    It ends the game if we are on the exit 
    It validates the user's move
'''
class Validator:
    
    def __init__(self):
        pass

    def validateInitMap(self, mapPlayed):
        
        if mapPlayed.maze.robot == None:
            raise RobocException ("No Robot Exception")

    def thisIsTheEnd(self, mapPlayed):
        return mapPlayed.maze.robot.equals(mapPlayed.maze.exit)
    
    def isOnTheEnd(self, mapPlayed, position):
        return position.equals(mapPlayed.maze.exit)
    
    def validateMove(self, mapPlayed, direction, steps):
        nexPositions = mapPlayed.maze.robot.getNextPositions(direction, steps)
        timesMove = 0
        for pos in nexPositions:
            if not self.validatePosition(mapPlayed, pos):
                return 0
            timesMove+=1
            if self.isOnTheEnd(mapPlayed, pos):
                return timesMove
        return timesMove;
    
    def validatePosition(self, mapPlayed, position):
        return mapPlayed.maze.isWalkingPoint(position)
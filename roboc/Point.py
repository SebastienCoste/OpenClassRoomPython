# -*-coding:Latin-1 -*
'''
Created on Feb 7, 2017
@author: Static
'''
from roboc.RobocException import RobocException
class Point:
    
    def __init__(self, height, width):
        self.height = height
        self.width = width
        
    def equals(self, point):
        return self.height == point.height and self.width == point.width
    
    def getNextPositions(self, direction, times):
        result = []
        copy = Point(self.height, self.width)
        for _ in range(times):
            copy = copy.getNext(direction)
            result.append(copy)
        
        return result
    
    '''
        Get the point to the next position
        No validation, except if the direction is not understandable
    '''
    def getNext(self, direction):
        nextPoint = Point(self.height, self.width)
        if (direction == 'DOWN'):
            nextPoint.height +=1
        elif (direction == 'UP'):
            nextPoint.height -=1
        elif (direction == 'LEFT'):
            nextPoint.width -=1
        elif (direction == 'RIGHT'):
            nextPoint.width +=1
        else:
            raise RobocException("Unknown Move Exception")
        return nextPoint

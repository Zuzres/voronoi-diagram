from .Point import Point
from math import sqrt

class Grain:
    def __init__(self, x:int, y:int, n:int):
        self.x = x
        self.y = y
        self.n = n
        self.points:set = set()
    
    def addPoint(self, x:int, y:int) -> None:
        self.points.add(Point(x, y))

    def getDistance(self, x:int, y:int) -> float:
        return sqrt(pow(x - self.x, 2) + pow(y - self.y, 2))
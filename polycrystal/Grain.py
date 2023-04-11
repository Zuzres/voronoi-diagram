from .Point import Point
from .Core import Core
from math import sqrt

class Grain:
    def __init__(self, core:Core):
        self.core = core
        self.points:set = set()
    
    def addPoint(self, x:int, y:int) -> None:
        self.points.add(Point(x, y))

    def getDistance(self, x:int, y:int) -> float:
        return sqrt(pow(x - self.core.x, 2) + pow(y - self.core.y, 2))
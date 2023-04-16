from random import randint
from math import sqrt
from . import Grain, Point
from matplotlib import pyplot as plt
import numpy as np

class PolyFactory:
    def __init__(self, sizeX, sizeY):
        self.sizeX:int = sizeX
        self.sizeY:int = sizeY
        self.grains:list = list()

    def seedGrains(self, numOfCores:int):
        """
            Generates a requested number of Grains 
            within the set size of polycrystal coordinates
        """
        self.grains.clear()

        # while len(self.grains) < numOfCores:
        for n in range(0, numOfCores):
            x = randint(0, self.sizeX)
            y = randint(0, self.sizeY)
            self.grains.append(Grain(x=x, y=y, n=n+1))        
    
    def growGrains(self):
        """
            Creates instances of Grain class 
            and grows them with body represented by points on a coordinates
            with x: 0 .... self.sizeX 
            and y: 0 .... self.sizeY
        """

        # then, start growing grains:
        for y in range(0, self.sizeY):
            for x in range(0, self.sizeX):
                growingGrain:Grain = self.grains[0]
                for grain in self.grains:
                    grain:Grain
                    distance = sqrt(pow(x - grain.x, 2) + pow(y - grain.y, 2))
                    if distance <= growingGrain.getDistance(x, y):
                        growingGrain = grain
                growingGrain.addPoint(x, y)

    def showGrains(self):
        """
            Puts all Points from the different Grains to a matrix 
            with the assigned numbers that equal to the corresponding core numbers.
            and finally shows the plot
        """

        colorMatrix = np.zeros((self.sizeX, self.sizeY))

        fig, ax = plt.subplots()
        
        for grain in self.grains:
            grain:Grain 
            for point in grain.points:
                point:Point
                colorMatrix[point.x, point.y] = grain.n
        
        ax.imshow(colorMatrix, cmap='Spectral')
        plt.show()
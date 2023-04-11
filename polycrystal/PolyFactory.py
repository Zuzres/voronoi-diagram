from collections.abc import Iterable
from random import randint
from math import sqrt
from . import Core, Grain, Point
from matplotlib import cm, pyplot as plt
import numpy as np

class PolyFactory:
    def __init__(self, sizeX, sizeY):
        self.sizeX:int = sizeX
        self.sizeY:int = sizeY
        self.cores:list = list()
        self.grains:list = list()

    def seedCores(self, numOfCores:int, normalizationFactor = 1) -> Iterable[Core]:
        """
            Generates a requested number of Cores 
            within the set size of polycrystal coordinates
            max distance between cores can be normalized 
            not to exceed the 1/Nth of size of the crystal.
        """
        max_dist_x = self.sizeX / normalizationFactor
        max_dist_y = self.sizeX / normalizationFactor
        while len(self.cores) < numOfCores:
            x = randint(0, self.sizeX)
            y = randint(0, self.sizeY)
            if normalizationFactor > 1 and \
                all(abs(x - core.x) > max_dist_x or \
                    abs(y - core.y) > max_dist_y for core in self.cores):
                self.cores.append(Core(x=x, y=y, n=len(self.cores) + 1))
            else:
                self.cores.append(Core(x=x, y=y, n=len(self.cores) + 1))
            
        return self.cores
    
    def growGrains(self) -> Iterable[Grain]:
        """
            Creates instances of Grain class 
            and grows them with body represented by points on a coordinates
            with x: 0 .... self.sizeX 
            and y: 0 .... self.sizeY
        """
        
        # first, create empty grains out of cores:
        for core in self.cores:
            grain:Grain = Grain(core)
            self.grains.append(grain)

        # then, start growing grains:
        for y in range(0, self.sizeY):
            for x in range(0, self.sizeX):
                growingGrain:Grain = self.grains[0]
                for grain in self.grains:
                    grain:Grain
                    distance = sqrt(pow(x - grain.core.x, 2) + pow(y - grain.core.y, 2))
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
            core:Core = grain.core
            for point in grain.points:
                point:Point
                colorMatrix[point.x, point.y] = core.n
        
        ax.imshow(colorMatrix, cmap='Spectral')
        plt.show()
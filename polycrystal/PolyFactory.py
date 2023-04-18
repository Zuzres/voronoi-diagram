from math import sqrt
from . import Grain, Point
from matplotlib import pyplot as plt
from numpy import zeros
from numpy.random import randint

class PolyFactory:
    def __init__(self, sizeX, sizeY):
        self.sizeX:int = sizeX
        self.sizeY:int = sizeY
        self.grains:list = list()

    def seedGrains(self, numGrains:int):
        """
            Generates a requested number of Grains 
            within the set size of polycrystal coordinates
        """
        self.grains.clear()
        
        # let's generate a collection of random (x,y) coordinates:
        coordinates = zip(
            randint(0, self.sizeX, numGrains, 'int'), 
            randint(0, self.sizeY, numGrains, 'int'))
        
        # now we can iterate through that (x, y) collection
        # and create a Grain instance for each of them:
        for i, (x, y) in enumerate(coordinates):
            self.grains.append(Grain(x=x, y=y, n=i+1))
    
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
                closestGrain:Grain = min(self.grains, key = lambda grain: \
                                  sqrt(pow(x - grain.x, 2) + pow(y - grain.y, 2)))
                closestGrain.addPoint(x, y)

    def showGrains(self):
        """
            Puts all Points from the different Grains to a matrix 
            with the assigned numbers that equal to the corresponding core numbers.
            and finally shows the plot
        """

        colorMatrix = zeros((self.sizeX, self.sizeY))

        fig, ax = plt.subplots()
        
        for grain in self.grains:
            grain:Grain 
            for point in grain.points:
                point:Point
                colorMatrix[point.x, point.y] = grain.n
        
        ax.imshow(colorMatrix, cmap='Spectral')
        plt.show()
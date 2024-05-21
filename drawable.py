#bb3323 Bavanan Bramillan

import pygame
from abc import ABC

class Drawable(ABC):
    def __init__(self, x=0, y=0, visible = True):
        self.__x = x 
        self.__y = y  
        self.__visible = visible

    def draw(self, surface):
        pass

    def get__rect(self):
        return pygame.Rect(0, 0, 0, 0)

    def getLoc(self):
        return (self.getX(), self.getY())

    def setX(self, x):
        self.__x = x 

    def setY(self, y):
        self.__y = y

    def getX(self):  
        return self.__x

    def getY(self):  
        return self.__y
 
    def isVisible(self):
        return self.__visible
    
    def setVisible(self, visible):
        if visible == True:
            self.__visible = True
        else:
            self.__visible = False

    def isTouching(self, other):
        pass


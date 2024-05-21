#bb3323 Bavanan Bramillan

import pygame
from drawable import Drawable

class Paddle(Drawable):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y)
        self.__color = color
        self.__width = width
        self.__height = height 

    def draw(self, surface):
        pygame.draw.rect(surface, self.__color, self.get__rect())

    def get__rect(self):
        surface = pygame.display.get_surface()
        screenWidth, screenHeight = surface.get_size()
        return pygame.Rect(self.getX() - self.getWidth() / 2, self.getY() - self.getHeight() / 2, self.getWidth(), self.getHeight())

    def getWidth(self):
        return self.__width
    
    def getHeight(self):
        return self.__height

    def update_position(self, mouseX):
        surface = pygame.display.get_surface()
        screenWidth, _ = surface.get_size()
        if mouseX - self.__width / 2 >= 0 and mouseX + self.__width / 2 <= screenWidth:
            self.setX(mouseX)

    


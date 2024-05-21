#bb3323 Bavanan Bramillan

import pygame, random
from drawable import Drawable

class Ball(Drawable):
    def __init__(self, x=0, y=0, color=(0,0,0), radius=30):
        super().__init__(x, y) 
        self.__color = color  
        self.__radius = radius
        self.__x_speed = 5 * random.choice([-1, 1])
        self.__y_speed = 5 * random.choice([-1, 1])

    def draw(self, surface):
        if self.isVisible(): 
            pygame.draw.circle(surface, self.__color, self.getLoc(), self.__radius)
    
    def get__rect(self):
        location = super().getLoc()  
        radius = self.__radius 
        return pygame.Rect(location[0] - radius, location[1] - radius, 2 * radius, 2 * radius) 

    def move(self):
        new_x = self.getX() + self.__x_speed
        new_y = self.getY() + self.__y_speed
        self.setX(new_x)
        self.setY(new_y)

    def check_collision(self, screen_width, screen_height):
        # Check collision with top and bottom walls
        if self.getY() - self.__radius <= 0 or self.getY() + self.__radius >= screen_height:
            self.__y_speed *= -1  # Reverse in y dir
            return True

        # Check collision with side walls
        if self.getX() - self.__radius <= 0 or self.getX() + self.__radius >= screen_width:
            self.__x_speed *= -1  # Reverse in x dir
            return False

    def getRadius(self):
        return self.__radius
    
    def getXSpeed(self):
        return self.__x_speed
    
    def getYSpeed(self):
        return self.__y_speed
    
    def setYSpeed(self, speed):
        self.__y_speed = speed
    
    def setXSpeed(self, speed):
        self.__x_speed = speed

    def isTouching(self, paddle):
        ball_rect = self.get__rect()
        paddle_rect = paddle.get__rect()
        return ball_rect.colliderect(paddle_rect)

   



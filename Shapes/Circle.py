import pygame
import random
import math



RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)


class Circle():
    def __init__(self,window,maxWidth,maxHeight):
        self.window = window
        self.color = random.choice((RED,GREEN,BLUE))
        self.radius = random.randrange(10,50)
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)
        self.centerX = self.x + self.radius
        self.centerY = self.y + self.radius
        self.rect = pygame.Rect(self.x, self.y,
                                self.radius * 2, self.radius * 2)
        self.shapeType = "Circle"
        

        self.centerX = random.randint(self.radius, maxWidth - self.radius)
        self.centerY = random.randint(self.radius, maxHeight - self.radius)


    # def clickedInside():
        
    def getArea(self):
        theArea = math.pi * self.radius**2
        return theArea
    
    def getShape(self):
        return self.shapeType

    def draw(self):
        pygame.draw.circle(self.window,self.color,self.rect) 
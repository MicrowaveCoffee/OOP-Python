import random
import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Triangle():
    def __init__(self,window, maxWidth,maxHeight):
        self.window = window
        self.height = random.randrange(10, 50)
        self.width = random.randrange(10, 50)

        self.color = random.choice((RED,GREEN,BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)

        self.rect = pygame.Rect(self.x,self.y,self.width,self.height)
        self.shapeType = "Triangle"


    def clickedInside(self,mousePoint):
        inRect = self.rect.collidepoint(mousePoint)
        if not inRect: 
            return False

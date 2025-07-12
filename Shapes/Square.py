import pygame 
import random

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Square():
    def __init__(self,window,maxHeight, maxWidth):
        self.window = window
        self.widthAndHeight = random.randrange(10,100)
        self.color = random.choice((RED,GREEN,BLUE))
        self.x = random.randrange(1, maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)
        self.shapeType = 'Square'
        self.rect = pygame.Rect(self.x,self.y,self.widthAndHeight,self.widthAndHeight)
        

    def getArea(self):
        theArea = self.widthAndHeight * self.widthAndHeight
        return theArea
    
    def getType(self):
        return self.shapeType
    
    def clickedInside(self,mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked
    
    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect)


pygame.init()
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Square Game")


clock = pygame.time.Clock()

squares = []
for i in range(5):
    square = Square(window, WIDTH, HEIGHT)
    squares.append(square)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            for square in squares:
                if square.clickedInside(mouse_pos):
                    print(f"Clicked on {square.getType()} with area {square.getArea()}")

    window.fill("WHITE")

    for square in squares:
        square.draw()
    
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
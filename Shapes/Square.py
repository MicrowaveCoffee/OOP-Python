import random
import pygame

RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)

class Square():
    def __init__(self,window,maxWidth,maxHeight):
        self.window = window
        self.color = random.choice((RED,GREEN,BLUE))
        self.heightAndWidth = random.randrange(10,100)
        self.x = random.randrange(1,maxWidth - 100)
        self.y = random.randrange(25, maxHeight - 100)
        self.rect = pygame.Rect(self.x,self.y,self.heightAndWidth,self.heightAndWidth)
        self.shapeType = 'Square'

    def getArea(self):
        theArea = self.heightAndWidth * self.heightAndWidth
        return theArea
    
    def getType(self):
        return self.shapeType
        
    
    def clickedInside(self, mousePoint):
        clicked = self.rect.collidepoint(mousePoint)
        return clicked
    
    def draw(self):
        pygame.draw.rect(self.window, self.color,
                         (self.x,self.y,self.heightAndWidth,self.heightAndWidth))



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
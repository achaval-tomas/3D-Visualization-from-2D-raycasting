from pygame import draw
from maths import *
# import random

class Boundary:
    def __init__(self, x1, y1, x2, y2):
        self.a = Vector2(x1, y1)
        self.b = Vector2(x2, y2)
        self.i = 40
    
    def light(self, val):
        maxdiag = sqrt(2*720*720)+1
        if val <= maxdiag:
            self.i = maprange(val, 0, maxdiag, 255, 0)
        else :
            self.i = 40
    
    def unlit(self):
        self.i = 40

    def draw(self, screen):
        draw.line(screen, (self.i, self.i, self.i), self.a, self.b, 10)

    def place(screen, walls) :
        for wall in walls :
            wall.draw(screen)
            wall.unlit()

    def setup(w, h):

        ''' RANDOM SETUP
        for i in range(0, 5):
            x1 = random.randrange(0, swidth)
            y1 = random.randrange(0, sheight)
            x2 = random.randrange(0, swidth)
            y2 = random.randrange(0, sheight)
            walls.append(Boundary(x1, y1, x2, y2))
        '''

        '''                COOL SETUP                '''
        walls = []
        walls.append(Boundary(w*0.8, 100,  w*0.6, 300 ))
        walls.append(Boundary(w*0.8,   0,  w*0.8,  60 ))
        walls.append(Boundary(w*0.6, 400,  w*0.8, 600 ))
        walls.append(Boundary(w*0.8, 720, w*0.8, 660 ))

        walls.append(Boundary( w/2, 300, w/2, 400 ))
        walls.append(Boundary( w/3, 100, w/3, 620 ))
        walls.append(Boundary(   0, 360, w/4, 360 ))
        walls.append(Boundary( w/4, 620, w/2, 620 ))
        
        walls.append(Boundary(  0,  0,  w,  0 ))
        walls.append(Boundary(  0,  0,  0,  h*3/4))
        walls.append(Boundary(  0, h*7/8 ,  0, h))
        walls.append(Boundary(  0,  h,  w,  h ))
        walls.append(Boundary(  w,  0,  w,  h ))

        return walls
    

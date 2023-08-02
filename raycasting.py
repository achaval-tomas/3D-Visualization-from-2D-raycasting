import pygame
from maths import *
from boundary import *
from ray import *
from lightsource import *

pygame.init()

# window width and height
fullSwidth  = 1440
fullSheight = 720

# half-window width and height
swidth = fullSwidth/2
sheight = fullSheight

# maximum possible ray length
maxdiag = sqrt(swidth*swidth + sheight*sheight) + 1

# window pop-up
screen = pygame.display.set_mode((fullSwidth, fullSheight))
pygame.display.set_caption('3D world form 2D Ray Casting')

# initialize simulation's objects
walls = Boundary.setup(swidth, sheight)
source = Source(30, 30)

# handle key inputs
def keyActions():
    keys = pygame.key.get_pressed()
    if keys[pygame.K_d]:
         source.rotate(1)
    elif keys[pygame.K_a]:
        source.rotate(-1)

    if keys[pygame.K_s]:
        source.move(-1)
    elif keys[pygame.K_w]:
        source.move(1)
    
    if keys[pygame.K_f]:
        source.updateFOV()

# render an individual wall piece
def wallpiece(i, w, h, c):
    pygame.draw.rect(screen, (c,c,c), (swidth+i*w, swidth/2 - h, w+1, 2*h))

    pygame.draw.line(screen,          (0,0,0), (swidth+i*w, swidth/2 - h), (swidth+i*w + w,swidth/2 - h), 4)
    pygame.draw.line(screen, "darkolivegreen", (swidth+i*w, swidth/2 + h), (swidth+i*w + w,swidth/2 + h), 4)

# render walls from an ordered array of ray lengths
def render3D(scene):
    pygame.draw.rect(screen,    "deepskyblue2", (swidth,         0, swidth, sheight/2))
    pygame.draw.rect(screen, "darkolivegreen4", (swidth, sheight/2, swidth, sheight/2))
    w = swidth / scene.__len__()
    for i in range(0, scene.__len__()) :
        if scene[i] < maxdiag :
            color = maprange(scene[i], 0, maxdiag,      255, 0)
            h     = maprange(scene[i], 0, maxdiag, swidth/2, 0)
        else:
            color = 0
            h     = 0
        wallpiece(i, w, h, color)

# initialize loop properties
clock = pygame.time.Clock()
running = True
framerate = 60

'''                                 MAIN LOOP                                       '''
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keyActions()                            # move and rotate the light source

    render3D(source.emit(screen, walls))    # render 3D simulation from emmited rays

    Boundary.place(screen, walls)           # render 2D upper view of boundaries

    pygame.display.flip()                   # display all renders on screen

    clock.tick(framerate)

pygame.quit()
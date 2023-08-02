from math import *
from pygame import Vector2

# map a number from range (a,b) to range (c, d)
def maprange(x, a, b, c, d):
    w =  (x-a) / (b-a)
    y = c + w * (d-c)
    return y

def vecToAngle(vect):
    return atan(vect.y/vect.x)

def degsToVec(angle):
    a = angle*pi/180
    return Vector2(cos(a), sin(a))

def radians(degs):
    return degs*pi/180
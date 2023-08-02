from pygame import draw
from boundary import *
from maths import *

class Ray:
    def __init__(self, pos, angle):
        self.pos = pos
        self.dir = degsToVec(angle)
    
    def draw(self, screen):
        draw.line(screen, "white", self.pos, self.pos + self.dir, 1)

    def lookAt(self, x, y) :
        self.dir = Vector2(x, y) - self.pos
        self.dir.normalize()
    
    def setAngle(self, angle):
        self.dir = degsToVec(angle)
    
    def getAngle(self):
        return vecToAngle(self.dir)

    def cast(self, wall):
        x1 = wall.a.x
        y1 = wall.a.y
        x2 = wall.b.x
        y2 = wall.b.y

        x3 = self.pos.x
        y3 = self.pos.y
        x4 = self.pos.x + self.dir.x
        y4 = self.pos.y + self.dir.y

        den = (x1-x2) * (y3-y4) - (y1-y2) * (x3-x4)

        if den!=0 :
            t =  ( (x1-x3) * (y3-y4) - (y1-y3) * (x3-x4) ) / den
            u = -( (x1-x2) * (y1-y3) - (y1-y2) * (x1-x3) ) / den

            if (t > 0) & (t < 1) & (u > 0) :
                return Vector2( (x1 + t*(x2-x1)), (y1 + t*(y2-y1)) )
    
        return
        

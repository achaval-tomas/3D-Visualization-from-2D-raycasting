from pygame import draw
from ray import *
from maths import *

class Source:
    def __init__(self, x, y):
        self.pos = Vector2(x, y)
        self.rays = []
        self.fov = 30
        self.heading = 45
        self.setRays()
    
    def setRays(self) :
        self.rays = []
        for a in range(self.heading - self.fov, self.heading + self.fov):
            for i in range(0,3):
                self.rays.append(Ray(self.pos, a+i/4))

    def rotate(self, angle):
        self.heading = (self.heading % 360) + angle*2
        self.setRays()
    
    def move(self, val):
        vel = degsToVec(self.heading)*val
        self.pos += vel*2
        self.setRays()
    
    def update(self, x, y):
        self.pos = Vector2(x, y)
        self.setRays()
    
    def updateFOV(self, dir):
        self.fov = dir + (self.fov % 90)
        if self.fov == 0:
            self.fov = 1
        self.setRays()

    def castall(self, screen, walls):
        scene = []

        for ray in self.rays:
            closest = None
            record = inf
            closestWall = None
            for wall in walls:
                pt = ray.cast(wall) 
                if pt :
                    d = dist(self.pos, pt)
                    d *= abs(cos(ray.getAngle() - radians(self.heading)))
                    if record > d :
                        record =  d
                        closest = pt
                        closestWall = wall
                    
            if closest :
                closestWall.light(record)
                draw.line(screen, "white", self.pos, closest, 1)
            
            scene.append(record)

        return scene

    def emit(self, screen, walls):
        screen.fill("darkolivegreen4")
        scene = self.castall(screen, walls)
        draw.circle(screen, "darkred", self.pos, 16)
        return scene

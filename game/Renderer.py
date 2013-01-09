import pygame
from pygame.gfxdraw import *
from pygame.locals import Color
from game.components.Transform import Transform, NullTransform
import math

class Renderer:
    def __init__(self):
        self.surface = None
        self.color = Color(0, 0, 0)
        self.clearColor = Color(0, 0, 0)
        self.transform = Transform()
        
        self.antialiasing = False

    def init(self, size):
        self.surface = pygame.display.set_mode(size, pygame.DOUBLEBUF|pygame.HWSURFACE)

    def begin(self):
        self.surface.fill(self.clearColor)
        
    def end(self):
        pygame.display.update()

    def setColor(self, color):
        self.color = color
        
    def setTransform(self, transform):
        self.transform = transform
    
    def renderLine(self, v1, v2):
        a = self._transformVertex(v1)
        b = self._transformVertex(v2)
        line(self.surface, a[0], a[1], b[0], b[1], self.color)
        
    def renderCircle(self, center, radius):
        center = self._transformVertex(center)
        if self.antialiasing:
            aacircle(self.surface, center[0], center[1], radius, self.color)
        else:
            circle(self.surface, center[0], center[1], radius, self.color)

    def renderFilledPolygon(self, polygon):
        filled_polygon(self.surface, map(self._transformVertex, polygon), self.color)

    def renderPolygon(self, polygon):
        if(self.antialiasing):
            aapolygon(self.surface, map(self._transformVertex, polygon), self.color)
        else:    
            for vid in range(-1, len(polygon) - 1):
                v1 = polygon[vid]
                v2 = polygon[vid + 1]
                self.renderLine(v1, v2)

    def renderMesh(self, mesh):
        self.setTransform(mesh.transform)
        self.renderPolygon(mesh.vertices)        
        self._resetTransform()
    
    def _resetTransform(self):
        self.transform = NullTransform
    
    def _transformVertex(self, vertex):
        v = [vertex[0], vertex[1]]
        sin = math.sin(self.transform.rotation)
        cos = math.cos(self.transform.rotation)

        # rotate
        x = v[0]
        y = v[1]
        v[0] = x * cos - y * sin
        v[1] = x * sin + y * cos
        # scale
        v[0] *= self.transform.scale[0]
        v[1] *= self.transform.scale[1]
        
        # translate
        v[0] += self.transform.translation[0]
        v[1] += self.transform.translation[1]

        return (int(v[0]), int(v[1]))

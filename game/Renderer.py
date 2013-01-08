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
        self.surface = pygame.display.set_mode(size)

    def begin(self):
        self.surface.fill(self.clearColor)
        
    def end(self):
        pygame.display.update()

    def setColor(self, color):
        self.color = color
        
    def setTransform(self, transform):
        self.transform = transform
    
    def renderLine(self, v1, v2):
        line(self.surface, v1[0], v1[1], v2[0], v2[1], self.color)
        
    def renderCircle(self, center, radius):
        center = self._transformVertex(center)
        if self.antialiasing:
            aacircle(self.surface, center[0], center[1], radius, self.color)
        else:
            circle(self.surface, center[0], center[1], radius, self.color)

    def renderMesh(self, mesh):
        self.setTransform(mesh.transform)

        if(self.antialiasing):
            aapolygon(self.surface, map(self._transformVertex, mesh.vertices), self.color)
        else:    
            for vid in range(-1, len(mesh.vertices) - 1):
                v1 = self._transformVertex(mesh.vertices[vid])
                v2 = self._transformVertex(mesh.vertices[vid + 1])
                self.renderLine(v1, v2)
        
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

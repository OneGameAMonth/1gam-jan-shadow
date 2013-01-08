import sys
import os.path
oldpath = sys.path[:]
sys.path.append(os.path.split(os.path.dirname(os.path.realpath(__file__)))[0])

import pygame
from pygame.locals import *
from pygame.rect import *

from game.Renderer import Renderer
from game.Mesh import Mesh
from game.Light import *

from game import Shadow

pygame.init()


renderer = Renderer()
renderer.init((800, 600))
renderer.antialiasing = False
renderer.color = Color(200, 100, 0)
renderer.clearColor = Color(31, 32, 34)

mesh = Mesh()
mesh.vertices = [ (-50, -30), (0, 50), (50, -30) ]
mesh.transform.translation = (200, 200)

sh = Shadow.createShadow(mesh, Light(LightType.SPOTLIGHT))


while(True):
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    mesh.transform.rotation += 0.001

    renderer.begin()
    renderer.renderMesh(mesh)
    renderer.setTransform(mesh.transform)
    renderer.renderCircle(mesh.origin, 3)
    renderer.end()

sys.path = oldpath

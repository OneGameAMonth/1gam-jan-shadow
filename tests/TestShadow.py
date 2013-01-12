import sys
import pygame
from pygame.locals import *
from pygame.time import Clock

from game.Renderer import Renderer
from game import Shadow
from game.Geometry import Vec2
from game.components.Transform import *
from game.Mesh import *

renderer = Renderer()

triangle_vertices = [ Vec2(0, 50), Vec2(-50, -30), Vec2(50, -30) ]
quad_vertices = [ Vec2(-20, -20), Vec2(20, -20), Vec2(20, 20), Vec2(-20, 20) ]

Triangle1 = Mesh( triangle_vertices )
Triangle1.transform = Transform(translation=(400, 300))

meshes = [ Triangle1 ]

mousePosition = (0, 0)

def initialize():
    global renderer
    pygame.init()
    
    pygame.display.set_caption("Shadow")
    pygame.mouse.set_visible(False)
    
    renderer = Renderer()
    renderer.init((800, 600))
    renderer.antialiasing = False
    renderer.clearColor = Color(31, 32, 34)
    renderer.color = Color(200, 100, 0)

def renderLightSource():
    renderer.setTransform(NullTransform)
    renderer.color = Color(200, 100, 10)
    renderer.renderCircle(mousePosition, 3)

def renderShadows(mesh):
    renderer.setTransform( mesh.transform )
    renderer.color = Color(20, 21, 22)
    light = Vec2.fromTuple(mousePosition) - Vec2.fromTuple(mesh.transform.translation)
    Shadow.renderShadow(renderer, mesh.vertices, light)
    
def renderSurface(mesh):
    renderer.setTransform( mesh.transform )
    renderer.color = Color(200, 100, 10)
    renderer.antialiasing = True
    renderer.renderFilledPolygon(mesh.vertices)
    renderer.antialiasing = False

def render():
    renderer.begin()
    renderLightSource()
    
    for m in meshes:
        renderShadows(m)
        
    for m in meshes:
        renderSurface(m)
    
    renderer.end()
    
def handleEvent(event):
    global mousePosition
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    if event.type == MOUSEMOTION:
        mousePosition = event.pos
    if event.type == MOUSEBUTTONDOWN:
        m = Mesh( quad_vertices )
        m.transform.translation = mousePosition
        meshes.append(m)
    
def update():
    for event in pygame.event.get():
        handleEvent(event)

def run():
    clock = Clock()
    initialize()
    while(True):
        dt = clock.tick(60)
        update()
        render()

if __name__ == "__main__":
    run()

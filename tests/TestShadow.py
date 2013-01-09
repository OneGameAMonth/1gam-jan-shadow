import sys
import pygame
from pygame.locals import *
from pygame.time import Clock

from game.Renderer import Renderer
from game import Shadow
from game.Geometry import Vec2
from game.components.Transform import *

renderer = Renderer()
Vertices = [ (0, 50), (-50, -30), (50, -30) ]
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
    
def renderShadows():
    renderer.color = Color(20, 21, 22)
    light = Vec2.fromTuple(mousePosition) - Vec2(400, 300)
    v = map( lambda x: Vec2.fromTuple(x), Vertices)
    shape = Shadow.projectEdge( v[0], v[1], light)
    renderer.renderFilledPolygon(shape)
    shape = Shadow.projectEdge( v[1], v[2], light)
    renderer.renderFilledPolygon(shape)
    shape = Shadow.projectEdge( v[0], v[2], light)
    renderer.renderFilledPolygon(shape)
    
def renderMesh():
    renderer.color = Color(200, 100, 10)
    renderer.antialiasing = True
    renderer.renderFilledPolygon(Vertices)
    renderer.antialiasing = False

def render():
    renderer.begin()
    renderLightSource()
    renderer.setTransform(Transform(translation=(400, 300)))
    renderShadows()    
    renderMesh()
    renderer.end()
    
def handleEvent(event):
    global mousePosition
    if event.type == QUIT:
        pygame.quit()
        sys.exit()
    if event.type == MOUSEMOTION:
        mousePosition = event.pos
    
def update():
    for event in pygame.event.get():
        handleEvent(event)

def run():
    clock = Clock()
    initialize()
    while(True):
        dt = clock.tick( 60 )
        update()
        render()

if __name__ == "__main__":
    run()
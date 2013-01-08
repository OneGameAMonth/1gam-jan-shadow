from game.Light import *
from game.Vector import Vec2

def createShadow(mesh, light):
    if light.type == LightType.SPOTLIGHT:
        return createShadowFromSpotLight(mesh, light)
    raise AssertionError("Shadow casting for light type {0} is not implemented".format(light.type))

def createShadowFromSpotLight(mesh, light):
    
    return []

def _getExtremityVertices(): 
    pass

def getShadowLength(vertex, origin):
    return (vertex - origin).length()

def _extrudeVertices(vertices, origin):
    newVertices = vertices[:]
    for v in reversed(vertices):
        v2 = Vec2.fromTuple(v)
        newVertices.append(projectVertex(v2, origin).toTuple())
    return newVertices
    
        
def projectVertex(point, light):
    return point + point - light

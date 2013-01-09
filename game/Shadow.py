from game.Light import *
from game.Geometry import Vec2
from game.components.Transform import Transform

def createShadow(mesh, light):
    if light.type == LightType.SPOTLIGHT:
        return createShadowFromSpotLight(mesh, light)
    raise AssertionError("Shadow casting for light type {0} is not implemented".format(light.type))

def createShadowFromSpotLight(mesh, light):
    
    return []

def _getExtremityVertices(): 
    pass

def getShadowLength(vertex, origin):
    return 1000
    #return (vertex - origin).length()

def projectVertices(vertices, origin):
    newVertices = vertices[:]
    for v in reversed(vertices):
        v2 = Vec2.fromTuple(v)
        newVertices.append(projectVertex(v2, origin).toTuple())
    return newVertices    
        
def projectVertex(point, light):
    return point + (point - light).normalized().scaled(getShadowLength(point, light))

def projectEdge(v1, v2, light):
    pv1 = projectVertex(v1, light)
    pv2 = projectVertex(v2, light)
    return [v1, v2, pv2, pv1]

def getEdgeNormal(v1, v2):
    t = Transform(rotation=90)
    return t.apply( v2 - v1 )
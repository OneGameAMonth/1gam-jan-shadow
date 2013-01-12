from game.Light import *
from game.Geometry import Vec2
from game.components.Transform import Transform

def getShadowLength(vertex, origin):
    return 1000
    #return (vertex - origin).length()

def _castsShadow(v1, v2, light):
    return True  # (v1 - light).normalized().dot(getEdgeNormal(v1,v2)) > 0

def _addToSortedSet(x, sortedset):
    if not (x in sortedset):
        sortedset.append(x)
    return sortedset

def renderShadow(renderer, polygon, light, length=getShadowLength):
    for vid in range(-1, len(polygon) - 1):
        v1 = polygon[vid]
        v2 = polygon[vid + 1]
        if _castsShadow(v1, v2, light):
            renderer.renderFilledPolygon(projectEdge(v1, v2, light))
            
    
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
    return t.apply(v2 - v1)

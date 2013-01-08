from game.Light import *

def createShadow(mesh, light):
    if light.type == LightType.SPOTLIGHT:
        return createShadowFromSpotLight(mesh, light)
    raise AssertionError("Shadow casting for light type {0} is not implemented".format(light.type))

def createShadowFromSpotLight(mesh, light):
    
    return []

def _getExtremityVertices(): 
    pass

def _extrude(vertices, point, length):
    pass

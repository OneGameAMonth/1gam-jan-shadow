class LightType:
    SPOTLIGHT = "SPOTLIGHT"
    DIRECTIONAL = "DIRECTIONAL"
    POINTLIGHT = "POINTLIGHT"
    NONE = "NONE"

class Light:
    def __init__(self, lightType=LightType.NONE):
        self.type = lightType

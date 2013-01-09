import math

class Transform:

    def __init__(self, **kwargs):
        if "translation" in kwargs:
            self.translation = kwargs["translation"]
        else:
            self.translation = (0, 0)
        
        if "rotation" in kwargs:
            self.rotation = kwargs["rotation"]
        else:    
            self.rotation = 0
            
        if "scale" in kwargs:
            self.scale = kwargs["scale"]
        else:
            self.scale = (1, 1)
        
    def apply(self, vertex):
        v = [vertex[0], vertex[1]]
        sin = math.sin(self.rotation)
        cos = math.cos(self.rotation)

        # rotate
        x = v[0]
        y = v[1]
        v[0] = x * cos - y * sin
        v[1] = x * sin + y * cos
        # scale
        v[0] *= self.scale[0]
        v[1] *= self.scale[1]
        
        # translate
        v[0] += self.translation[0]
        v[1] += self.translation[1]

        return (round(v[0]), round(v[1]))

NullTransform = Transform()

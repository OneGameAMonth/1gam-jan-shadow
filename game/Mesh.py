from game.components.Transform import Transform

class Mesh:
    def __init__(self, vertices = []):
        self.origin = (0, 0)
        self.vertices = vertices
        self.transform = Transform()

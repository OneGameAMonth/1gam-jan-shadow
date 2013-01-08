import math

class Vec2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return self +other.scaled(-1)
    
    def __getitem__(self, i):
        if i == 0:
            return self.x
        if i == 1:
            return self.y
        raise AttributeError("Vec2 has no such dimension {0}".format(i))
        
    def __str__(self):
        return "Vec2({0},{1})".format(self.x, self.y)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def cross(self, other):
        return self.x * other.y - other.x * self.y
    
    def length(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

    def normalized(self):
        l = self.length()
        return Vec2(self.x / l, self.y / l)

    def scaled(self, scalar):
        return Vec2(self.x * scalar, self.y * scalar)

    def toTuple(self):
        return (int(self.x), int(self.y))
    
    @staticmethod
    def fromTuple(t):
        return Vec2(t[0], t[1])

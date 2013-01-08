import math

class Vec2:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y
        
    def __add__(self, other):
        return Vec2(self.x + other.x, self.y + other.y)
    
    def __getitem__(self, i):
        if i == 0:
            return self.x
        if i == 1:
            return self.y
        raise AttributeError("Vec2 has no such dimension {0}".format(i));
    
    def __mul__(self, scalar):
        if type(scalar) == int:
            return Vec2(self.x * scalar, self.y * scalar)
        
    def __str__(self):
        return "Vec2({0},{1})".format(self.x, self.y)
    
    def dot(self, other):
        return self.x * other.x + self.y * other.y
    
    def cross(self, other):
        return self.x * other.y - other.x * self.y
    
    def len(self):
        return math.sqrt(self.x * self.x + self.y * self.y)

import unittest
import math
from game.Vector import Vec2

class TestVec2(unittest.TestCase):
    
    def setUp(self):
        self.v0 = Vec2(0, 0)
        self.v1 = Vec2(1, 1)
        self.v2 = Vec2(2, 3)

    def testAddition(self):
        v3 = self.v1 + self.v2
        self.assertEqual(v3, Vec2(3, 4))
        
    def testScalarMultiplication(self):
        v3 = self.v2 * 3
        self.assertEqual(v3, Vec2(6, 9))
        
    def testDotProduct(self):
        v3 = self.v2.dot(Vec2(4, 5))
        self.assertEqual(v3, 4 * 2 + 3 * 5)
    
    def testCrossProduct(self):
        v3 = self.v2.cross(Vec2(4, 5))
        self.assertEqual(v3, -2)

    def testLength(self):
        self.assertEqual(self.v0.len(), 0)
        self.assertEqual(self.v1.len(), math.sqrt(2))
        self.assertEqual(self.v2.len(), math.sqrt(13))

import unittest
import math
from game import Shadow
from game.Geometry import Vec2

class TestShadowModule(unittest.TestCase):
    
    def setUp(self):
        pass

    def testEdgeNormal(self):
        normal = Vec2.fromTuple(Shadow.getEdgeNormal(Vec2(5, 5), Vec2(5, 6)))
        self.assertEqual(normal, Vec2(-1, 0))
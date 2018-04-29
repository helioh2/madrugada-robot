import unittest, math
from madrugada_turtle import MadrugadaTurtle

class BluetoothSocketMock():

    def __init__(self, value=0):
        pass

    def send(self, data):
        print("Teste enviando ao bluetooth:", data)


class TestTurtle(unittest.TestCase):

    def setUp(self):
        self.sock = BluetoothSocketMock()
        self.turtle = MadrugadaTurtle(self.sock)

    def testForward(self):
        self.turtle.forward(50)
        self.assertEqual(self.turtle.x, 50)
        self.assertEqual(self.turtle.y, 0)

    def testBackward(self):
        self.turtle.backward(50)
        self.assertEqual(self.turtle.x, -50)
        self.assertAlmostEqual(self.turtle.y, 0)
    
    def testTurn(self):
        self.turtle.turn(45)
        self.assertEqual(self.turtle.angle, 45)

        self.turtle.forward(40)
        angle_rad = math.radians(45)
        dx = 40 * math.cos(angle_rad)
        dy = 40 * math.sin(angle_rad)
        self.assertEqual(self.turtle.x, dx)
        self.assertEqual(self.turtle.y, dy)

    def testpen_upDown(self):
        self.assertTrue(self.turtle.pen_is_down)
        self.turtle.pen_up()
        self.assertFalse(self.turtle.pen_is_down)
        self.turtle.pen_down()
        self.assertTrue(self.turtle.pen_is_down)

    def testGoTo(self):
        self.turtle.go_to(20,30)
        self.assertEqual(self.turtle.x, 20)
        self.assertEqual(self.turtle.y, 30)

    def testLimits(self):
        self.turtle.forward(self.turtle.xlimits[1] + 1)
        self.assertEqual(self.turtle.x, 0)
        
        self.turtle.turn(90)
        self.turtle.forward(self.turtle.ylimits[1] + 1)
        self.assertEqual(self.turtle.y, 0)

        self.turtle.turn(90)
        self.turtle.forward(self.turtle.xlimits[0] - 1)
        self.assertEqual(self.turtle.x, 0)

        self.turtle.turn(90)
        self.turtle.forward(self.turtle.ylimits[0] - 1)
        self.assertEqual(self.turtle.y, 0)


if __name__ == '__main__':
    unittest.main()

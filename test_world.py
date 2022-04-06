from io import StringIO
import unittest
from robot import *
from unittest.mock import patch
from io import StringIO
from world.text.world import *
from world.turtle.world import *
import maze.obstacles as obstacles


class MyTestCase(unittest.TestCase):

    @patch('sys.stdin',StringIO('xman\nforward 201\nforward 10\noff\n'))
    def test_range_of_y(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next? xman: Sorry, I cannot go outside my safe zone.
 > xman now at position (0,0).
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nleft\nforward 101\noff\n'))
    def test_range_of_x(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman turned left.
 > xman now at position (0,0).
xman: What must I do next? xman: Sorry, I cannot go outside my safe zone.
 > xman now at position (0,0).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())



    @patch('sys.stdin',StringIO('xman\nforward 10\noff\n'))
    def test_show_obstacle(self):
        self.maxDiff=None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 1
            robot_start()

        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: Loaded obstacles.
There are some obstacles:
- At position 1,1 (to 5,5)""", output.getvalue()[:132])



if __name__=='__main__':
    unittest.main()
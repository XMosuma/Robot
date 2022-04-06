from io import StringIO
import unittest
from robot import *
from unittest.mock import patch
from io import StringIO
import maze.obstacles as obstacles

class MyTestCase(unittest.TestCase):

    @patch('sys.stdin',StringIO('xman\noff\n'))
    def test_off(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\noFf\n'))
    def test_off_camelcase(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()

        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nJump up\noff\n'))
    def test_invalid_command(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next? xman: Sorry, I did not understand 'Jump up'.
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    def test_help(self):
        self.maxDiff = None
        obstacles.random.randint = lambda a, b: 0
        self.assertEqual("""I can understand these commands:\n\
OFF  - Shut down robot\n\
HELP - provide information about commands\n\
FORWARD - move the robot forward\n\
BACK - move the robot backward\n\
RIGHT - turn the robot right\n\
LEFT - turn the robot left\n\
SPRINT - sprint the robot\n\
HISTORY - displays history of commands\n\
REPLAY - replay the movement commands\n\
REPLAY SILENT - replay of the commands without showing output\n\
REPLAY REVERSED - play back the commands in reverse order\n\
REPLAY REVERSED SILENT - play back the commands in reverse without showing output\n\
MAZERUN — the robot figure out a short path to any end of the maze.\n""",\
    do_help())


    @patch('sys.stdin',StringIO('xman\nforward 10\noff\n'))
    def test_forward(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nback 10\noff\n'))
    def test_back(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved back by 10 steps.
 > xman now at position (0,-10).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 10\nright\nback 10\noff\n'))
    def test_forward_turn_right(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next?  > xman turned right.
 > xman now at position (0,10).
xman: What must I do next?  > xman moved back by 10 steps.
 > xman now at position (-10,10).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nback 10\nleft\nforward 10\noff\n'))
    def test_back_turn_left(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved back by 10 steps.
 > xman now at position (0,-10).
xman: What must I do next?  > xman turned left.
 > xman now at position (0,-10).
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (-10,-10).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nsprint 5\noff\n'))
    def test_sprint(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 5 steps.
 > xman moved forward by 4 steps.
 > xman moved forward by 3 steps.
 > xman moved forward by 2 steps.
 > xman moved forward by 1 steps.
 > xman now at position (0,15).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 10\nback 5'\
        '\nright\nforward 15\nreplay\noff\n'))
    def test_replay(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual('''What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next?  > xman moved back by 5 steps.
 > xman now at position (0,5).
xman: What must I do next?  > xman turned right.
 > xman now at position (0,5).
xman: What must I do next?  > xman moved forward by 15 steps.
 > xman now at position (15,5).
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (25,5).
 > xman moved back by 5 steps.
 > xman now at position (20,5).
 > xman turned right.
 > xman now at position (20,5).
 > xman moved forward by 15 steps.
 > xman now at position (20,-10).
 > xman replayed 4 commands.
 > xman now at position (20,-10).
xman: What must I do next? xman: Shutting down..\n''', output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 10\nforward 5\nreplay\nreplay\noff\n'))
    def test_replay_twice(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next?  > xman moved forward by 5 steps.
 > xman now at position (0,15).
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,25).
 > xman moved forward by 5 steps.
 > xman now at position (0,30).
 > xman replayed 2 commands.
 > xman now at position (0,30).
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,40).
 > xman moved forward by 5 steps.
 > xman now at position (0,45).
 > xman replayed 2 commands.
 > xman now at position (0,45).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 10\nback 5'\
        '\nright\nforward 15\nreplay silent\noff\n'))
    def test_replay_silent(self):

        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual('''What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next?  > xman moved back by 5 steps.
 > xman now at position (0,5).
xman: What must I do next?  > xman turned right.
 > xman now at position (0,5).
xman: What must I do next?  > xman moved forward by 15 steps.
 > xman now at position (15,5).
xman: What must I do next?  > xman replayed 4 commands silently.
 > xman now at position (20,-10).
xman: What must I do next? xman: Shutting down..\n''', output.getvalue())
       

    @patch('sys.stdin',StringIO('xman\nforward 10\nforward 5'\
        '\nREPLAY SILENT abd\nreplay silent\noff\n'))
    def test_replay_silent_invalid(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next?  > xman moved forward by 5 steps.
 > xman now at position (0,15).
xman: What must I do next? xman: Sorry, I did not understand 'REPLAY SILENT abd'.
xman: What must I do next?  > xman replayed 2 commands silently.
 > xman now at position (0,30).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 10\nforward 5\nreplay reversed\noff\n'))
    def test_step4_replay_reversed(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next?  > xman moved forward by 5 steps.
 > xman now at position (0,15).
xman: What must I do next?  > xman moved forward by 5 steps.
 > xman now at position (0,20).
 > xman moved forward by 10 steps.
 > xman now at position (0,30).
 > xman replayed 2 commands in reverse.
 > xman now at position (0,30).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 10\nforward 5\nreplay REVERSE\noff\n'))
    def test_replay_reversed_invalid(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next?  > xman moved forward by 5 steps.
 > xman now at position (0,15).
xman: What must I do next? xman: Sorry, I did not understand 'replay REVERSE'.
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 10\nforward 5'\
        '\nreplay reversed silent\noff\n'))
    def test_replay_silent_reversed(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next?  > xman moved forward by 5 steps.
 > xman now at position (0,15).
xman: What must I do next?  > xman replayed 2 commands in reverse silently.
 > xman now at position (0,30).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 10\nforward 5'\
        '\nreplay REVERSED,SILENT\noff\n'))
    def test_replay_silent_reversed_invalid(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 10 steps.
 > xman now at position (0,10).
xman: What must I do next?  > xman moved forward by 5 steps.
 > xman now at position (0,15).
xman: What must I do next? xman: Sorry, I did not understand 'replay REVERSED,SILENT'.
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 3\nforward 2'\
        '\nforward 1\nreplay 2\noff\n'))
    def test_replay_2(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 3 steps.
 > xman now at position (0,3).
xman: What must I do next?  > xman moved forward by 2 steps.
 > xman now at position (0,5).
xman: What must I do next?  > xman moved forward by 1 steps.
 > xman now at position (0,6).
xman: What must I do next?  > xman moved forward by 2 steps.
 > xman now at position (0,8).
 > xman moved forward by 1 steps.
 > xman now at position (0,9).
 > xman replayed 2 commands.
 > xman now at position (0,9).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 3\nforward 2'\
        '\nforward 1\nreplay 3-1\noff\n'))
    def test_replay_range_3_1(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 3 steps.
 > xman now at position (0,3).
xman: What must I do next?  > xman moved forward by 2 steps.
 > xman now at position (0,5).
xman: What must I do next?  > xman moved forward by 1 steps.
 > xman now at position (0,6).
xman: What must I do next?  > xman moved forward by 3 steps.
 > xman now at position (0,9).
 > xman moved forward by 2 steps.
 > xman now at position (0,11).
 > xman replayed 2 commands.
 > xman now at position (0,11).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 3\nforward 2'\
        '\nforward 1\nreplay 3--a\noff\n'))
    def test_replay_range_invalid(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 3 steps.
 > xman now at position (0,3).
xman: What must I do next?  > xman moved forward by 2 steps.
 > xman now at position (0,5).
xman: What must I do next?  > xman moved forward by 1 steps.
 > xman now at position (0,6).
xman: What must I do next? xman: Sorry, I did not understand 'replay 3--a'.
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 3\nforward 2'\
        '\nforward 1\nreplay 2 silent\noff\n'))
    def test_replay_2_silent(self):
        self.maxDiff = None
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 3 steps.
 > xman now at position (0,3).
xman: What must I do next?  > xman moved forward by 2 steps.
 > xman now at position (0,5).
xman: What must I do next?  > xman moved forward by 1 steps.
 > xman now at position (0,6).
xman: What must I do next?  > xman replayed 2 commands silently.
 > xman now at position (0,9).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


    @patch('sys.stdin',StringIO('xman\nforward 3\nforward 2'
    '\nforward 1\nreplay 2 reversed\noff\n'))
    def test_replay_2_reversed(self):
        with patch('sys.stdout',StringIO()) as output:
            obstacles.random.randint = lambda a, b: 0
            robot_start()
        self.assertEqual("""What do you want to name your robot? xman: Hello kiddo!
xman: What must I do next?  > xman moved forward by 3 steps.
 > xman now at position (0,3).
xman: What must I do next?  > xman moved forward by 2 steps.
 > xman now at position (0,5).
xman: What must I do next?  > xman moved forward by 1 steps.
 > xman now at position (0,6).
xman: What must I do next?  > xman moved forward by 2 steps.
 > xman now at position (0,8).
 > xman moved forward by 3 steps.
 > xman now at position (0,11).
 > xman replayed 2 commands in reverse.
 > xman now at position (0,11).
xman: What must I do next? xman: Shutting down..\n""", output.getvalue())


if __name__=='__main__':
    unittest.main() 
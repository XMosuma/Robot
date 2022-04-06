import unittest
import maze.obstacles as obs

class MyTestCase(unittest.TestCase):
    def test_get_obstacles(self):
        self.maxDiff = None
        obs.random.randint = lambda a, b: 1
        self.assertEqual([(1,1)],obs.get_obstacles())
    
    def test_is_position_blocked_return_true(self):
        self.maxDiff = None
        position = obs.get_obstacles()
        x =position[0][0]
        y = position[0][1]
        self.assertTrue(obs.is_position_blocked(x,y))
    
    def test_is_position_blocked_return_false(self):
        self.maxDiff = None
        position = obs.get_obstacles()
        x =position[0][0]-1
        y = position[0][1]
        self.assertFalse(obs.is_position_blocked(x,y))
        

    def test_is_path_blocked_return_true(self):
        self.maxDiff = None
        position = obs.get_obstacles()
        x1 = position[0][0]
        y1 = position[0][1]-1
        x2 = x1
        y2 = position[0][1]+1
        self.assertTrue(obs.is_path_blocked(x1,y1,x2,y2))


    def test_is_path_blocked_return_false(self):
        self.maxDiff = None
        position = obs.get_obstacles()
        x1 = position[0][0]-1
        y1 = position[0][1]
        x2 = position[0][0]
        y2 = y1
        self.assertFalse(obs.is_path_blocked(x1,y1,x2,y2))


if __name__=='__main__':
    unittest.main()
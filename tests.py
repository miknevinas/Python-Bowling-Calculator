######################
######## Tests #######
######################

import unittest
from unittest.mock import patch

from bowling import Scoreboard, Frame

class Test(unittest.TestCase):

    def setUp(self):
        self.scoreboard = Scoreboard(frames=[], shots=[], score=0)


    def test_eights(self):
        for pins in [8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0, 8, 0]:
            self.scoreboard.throw(pins)
        self.assertEqual(80, self.scoreboard.get_final_score())

        
    def test_strikes(self):
        for pins in [10,10,10,10,10,10,10,10,10,10,10,10]:
            self.scoreboard.throw(pins)
        self.assertEqual(300, self.scoreboard.get_final_score())

    
    def test_spares(self):
        for pins in [1,9,2,8,3,7,4,6,5,5,6,4,7,3,8,2,9,1,9,1,8]:
            self.scoreboard.throw(pins)
        self.assertEqual(161, self.scoreboard.get_final_score())
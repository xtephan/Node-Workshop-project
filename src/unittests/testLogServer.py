'''
Created on Sep 20, 2011

@author: xtephan
'''
import unittest
from server.logserver import LogServer

class Test(unittest.TestCase):


    def setUp(self):
        self.LS = LogServer()
        pass


    def tearDown(self):
        pass


    def test_sanity(self):
        self.assertEqual(self.LS.sanity(), 4, 'sanity failed')
        pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_sanity']
    unittest.main()
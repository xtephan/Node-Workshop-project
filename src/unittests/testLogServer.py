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


    def test_parsePackage(self):
        self.assertEqual(self.LS.parsePackage("1#101"), [1,5], 'parse 1 failed')
        self.assertEqual(self.LS.parsePackage("2#001"), [2,1], 'parse 2 failed')
        self.assertEqual(self.LS.parsePackage("3#111"), [3,7], 'parse 3 failed')
        self.assertEqual(self.LS.parsePackage("4#000"), [4,0], 'parse 4 failed')
        pass



if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test_sanity']
    unittest.main()
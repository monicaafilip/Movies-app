'''
Created on Dec 6, 2017

@author: Monica
'''
import unittest
from domain.rentersName import rentersName
class testRentersName(unittest.TestCase):
    def setUp(self):
        self.__nameCustomer="Michael"
        self.__noRents=10

    def tearDown(self):
        pass
    
    def testRentersName(self):
        self._rentersName=rentersName(self.__nameCustomer,self.__noRents)
        self.assertEqual(self.__nameCustomer,"Michael")
        self.assertEqual(self.__noRents,10)
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
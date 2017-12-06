'''
Created on Dec 5, 2017

@author: Monica
'''
import unittest
from domain.rentDTO import rentDTO


class testRentDTO(unittest.TestCase):


    def setUp(self):
        self._idR=1
        self._idC=2
        self._custName="Michael"
        self._idM=2
        self._movName="Divergent"
        self._noRents=2
        
    def tearDown(self):
        pass


    def testRentDTO(self):
        self._rentDTO=rentDTO(self._idR,self._idC,self._custName,self._idM,self._movName,self._noRents)
        self.assertEqual(self._idR,1)
        self.assertEqual(self._idC,2)
        self.assertEqual(self._custName,"Michael")
        self.assertEqual(self._idM,2)
        self.assertEqual(self._movName,"Divergent")
        self.assertEqual(self._noRents,2)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
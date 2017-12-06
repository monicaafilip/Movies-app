'''
Created on Dec 5, 2017

@author: Monica
'''
import unittest
from domain.rent import rent


class testRent(unittest.TestCase):


    def setUp(self):
        self.__id=1
        self.__movie=10
        self.__customer=100
        self.__status="rented"

    def tearDown(self):
        pass


    def testRent(self):
        self._rent=rent(self.__id,self.__movie,self.__customer)
        self.assertEqual(self.__id,1)
        self.assertEqual(self.__movie,10)
        self.assertEqual(self.__customer,100)
        self.assertEqual(self._rent,rent(self.__id,self.__movie,self.__customer))

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
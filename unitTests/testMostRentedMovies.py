'''
Created on Dec 6, 2017

@author: Monica
'''
import unittest
from domain.mostRentedMovies import rentedMovies
class testRentedMovies(unittest.TestCase):
    def setUp(self):
        self.__title="Divergent"
        self.__noRents=6

    def tearDown(self):
        pass

    def testRentedMovies(self):
        self._rentedMovies=rentedMovies(self.__title,self.__noRents)
        self.assertEqual(self.__title,"Divergent")
        self.assertEqual(self.__noRents,6)
        self._newRented=rentedMovies(self.__title,self.__noRents)
        self.assertEqual(self._rentedMovies,self._newRented)

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
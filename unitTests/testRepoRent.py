'''
Created on Dec 5, 2017

@author: Monica
'''
import unittest
from unitTests.testUnitRent import testRent
from repository.repository import repository


class testRepoRent(testRent):


    def setUp(self):
        testRent.setUp(self)
        self._repo=repository()

    def tearDown(self):
        testRent.tearDown(self)


    def testRepoRent(self):
        testRent.testRent(self)
        self._repo.store(self._rent)
        self.assertEqual(self._repo.sizeOfList(), 1)
        self.assertEqual(self._repo.get(1),self._rent)
        self.assertEqual(self._repo.find("id",1),[self._rent])
        self.assertEqual(self._repo.find("idM",10),[self._rent])
        self.assertEqual(self._repo.find("idC",100),[self._rent])
        self._repo.clearList()
        self.assertEqual(self._repo.sizeOfList(),0)
      


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
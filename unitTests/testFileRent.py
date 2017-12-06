'''
Created on Dec 5, 2017

@author: Monica
'''
import unittest
from unitTests.testUnitRent import testRent
from repository.fileRepository import fileRepository
from domain.rent import rent


class Test(testRent):


    def setUp(self):
        testRent.setUp(self)
        self._fileName="rent.txt"

    def tearDown(self):
        with open(self._fileName,"w") as f:
            f.write("")
        f.close()

    def testName(self):
        testRent.testRent(self)
        self._repo=fileRepository(self._fileName,rent.readFromStr,rent.writeToStr)
        self._another=rent(1,10,100)
        self._repo.store(self._another)
        self.assertEqual(self._repo.find("id",1)[0].getMovie(),10)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
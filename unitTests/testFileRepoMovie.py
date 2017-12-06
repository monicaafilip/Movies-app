'''
Created on Dec 5, 2017

@author: Monica
'''
import unittest
from unitTests.testMovie import testMovie
from repository.fileRepository import fileRepository
from domain.movie import movie
class TestFileRepoMovie(testMovie):
    def setUp(self):
        testMovie.setUp(self)
        self._fileName='mov.txt'

    def tearDown(self):
        with open(self._fileName,"w") as f:
            f.write("")
        f.close()

    def testFileRepo(self):
        testMovie.testMovie(self)
        self._repo=fileRepository(self._fileName,movie.readFromStr,movie.writeToStr)
        self._another=movie(10,"Divergent","action","The best")
        self._repo.store(self._another)
        self.assertEqual(self._repo.find("id",10)[0].getTitle(),"Divergent")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
'''
Created on Nov 26, 2017

@author: Monica
'''
from unitTests.testMovie import testMovie
from repository.repository import repository
class testRepoMovie(testMovie):
    def setUp(self):
        testMovie.setUp(self)
        self._repo=repository()
        
    def tearDown(self):
        testMovie.tearDown(self)
    
    def testMovieRepo(self):
        testMovie.testMovie(self)
        self._repo.store(self._movie)
        self.assertEqual(self._repo.sizeOfList(), 1)
        self.assertEqual(self._repo.get(1),self._movie)
        self.assertEqual(self._repo.find("id",1),[self._movie])
        self.assertEqual(self._repo.find("title","Divergent"),[self._movie])
        self.assertEqual(self._repo.find("genre","Action"),[self._movie])
        self._repo.clearList()
        self.assertEqual(self._repo.sizeOfList(),0)
      
        
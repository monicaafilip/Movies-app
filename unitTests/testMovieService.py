'''
Created on Nov 26, 2017

@author: Monica
'''
from unitTests.testRepoMovie import testRepoMovie
from repository.repository import repository
from service.serviceM import moviesService
from validator.validatorMovie import validatorMovie
from domain.movie import movie
import unittest
class testServiceMovie(testRepoMovie):
    def setUp(self):
        testRepoMovie.setUp(self)
        
    def tearDown(self):
        testRepoMovie.tearDown(self)
    
    def testServiceMovie(self):
        testRepoMovie.testMovieRepo(self)
        self._repoMovie=repository()
        self._validator=validatorMovie()
        self._service=moviesService(self._repoMovie,self._validator)
        self._service.createMovie(2,"Divergent","Action","Amazing")
        self.assertEqual(self._service.getNrMovies(),1)
        self._service.update(2,"Inception","Love","Wonderful")
        self._movie=movie(2,"Inception","Love","Wonderful")
        self.assertEqual(self._repoMovie.find("id",self._movie.getId()),[self._movie])
            
    if __name__ == "__main__":
        #    import sys;sys.argv = ['', 'Test.testName']
        unittest.main()
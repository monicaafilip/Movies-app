'''
Created on Dec 5, 2017

@author: Monica
'''
import unittest
from unitTests.testRepoRent import testRepoRent
from repository.repository import repository
from validator.validatorRent import validatorRent
from service.serviceR import rentsService
from domain.rent import rent
from domain.movie import movie
from domain.customer import customer


class testRentService(testRepoRent):


    def setUp(self):
        testRepoRent.setUp(self)


    def tearDown(self):
        testRepoRent.tearDown(self)


    def testRentService(self):
        testRepoRent.testRent(self)
        self._repoRent=repository()
        self._repoM=repository()
        self._repoC=repository()
        self._repoM.store(movie(12,"It","Horror","Orrible"))
        self._repoC.store(customer(13,"Tudor",1231121231231))
        
        self._validator=validatorRent()
        self._service=rentsService(self._repoM,self._repoC,self._repoRent,self._validator)
        self._service.createRent(10,12,13)
        self.assertEqual(self._service.getNrRents(),1)
        self._rent=rent(10,12,13)
        self.assertEqual(self._repoRent.find("id",self._rent.getId()),[self._rent])
            


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
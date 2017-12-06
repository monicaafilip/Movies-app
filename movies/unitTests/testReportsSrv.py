'''
Created on Dec 5, 2017

@author: Monica
'''
import unittest
from unitTests.testRentDTO import testRentDTO
from domain.rentDTO import rentDTO
from service.serviceReports import serviceReports
from repository.repository import repository
from domain.customer import customer
from domain.movie import movie
from domain.rent import rent


class testReports(testRentDTO):


    def setUp(self):
        testRentDTO.setUp(self)
        
    def tearDown(self):
        testRentDTO.tearDown(self)


    def testReports(self):
        testRentDTO.testRentDTO(self)
        repoM=repository()
        repoC=repository()
        repoR=repository()
        repoM.store(movie(11,"Inception","..",".."))
        repoC.store(customer(10,"James",1231231231231))
        repoR.store(rent(10,11,10))
        self._srv=serviceReports(repoR,repoC,repoM)
        self._newRentDTO=rentDTO(10,10,"James",11,"Inception",10)
        self.assertEqual(len(self._srv.createTheDTOList()),1)


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
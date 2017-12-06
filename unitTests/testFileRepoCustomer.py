'''
Created on Dec 5, 2017

@author: Monica
'''
import unittest
from unitTests.testCustomer import testCustomer
from repository.fileRepository import fileRepository
from domain.customer import customer
class TestFileRepoCustomer(testCustomer):
    def setUp(self):
        testCustomer.setUp(self)
        self._fileName='cust.txt'

    def tearDown(self):
        with open(self._fileName,"w") as f:
            f.write("")


    def testFileRepo(self):
        testCustomer.testCustomer(self)
        self._repo=fileRepository(self._fileName,customer.readFromStr,customer.writeToStr)
        self._another=customer(10,"Ingrid",1010101010101)
        self._repo.store(self._another)
        self.assertEqual(self._repo.find("id",10)[0].getName(),"Ingrid")
        
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
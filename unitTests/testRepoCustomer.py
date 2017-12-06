'''
Created on Nov 26, 2017

@author: Monica
'''
from repository.repository import repository
from unitTests.testCustomer import testCustomer
class testRepoCustomer(testCustomer):
    def setUp(self):
        testCustomer.setUp(self)
        self._repo=repository()

    def tearDown(self):
        testCustomer.tearDown(self)

    def testCustomerRepo(self):
        testCustomer.testCustomer(self)
        self._repo.store(self._customer)
        self.assertEqual(self._repo.sizeOfList(), 1)
        self.assertEqual(self._repo.get(1),self._customer)
        self.assertEqual(self._repo.find("id",1),[self._customer])
        self.assertEqual(self._repo.find("name","Michael"),[self._customer])
        self._repo.clearList()
        self.assertEqual(self._repo.sizeOfList(),0)

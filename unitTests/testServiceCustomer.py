'''
Created on Nov 27, 2017

@author: Monica
'''
from unitTests.testRepoCustomer import testRepoCustomer
from repository.repository import repository
from validator.validatorCustomer import validatorCustomer
from service.serviceC import customersService

class testServiceCustomer(testRepoCustomer):

    def setUp(self):
        return testRepoCustomer.setUp(self)


    def tearDown(self):
        return testRepoCustomer.tearDown(self)


    def testServiceCustomer(self):
        return testRepoCustomer.testCustomer(self)
        self.__repoCustomer=repository()
        self.__validator=validatorCustomer()
        self._service=customersService(self.__repoCustomer,self.__validator)
        self._service.createCustomer(2,"John",2991010343434)
        self.assertEqual(self._service.getNrCustomers(),1)
    
        ''' black box testing'''
        try:
            self._service.createCustomer(2,"Laur",2991010343436)
            assert False
        except ValueError:
            assert True
            
        try:
            self._service.createCustomer(4,"Laur",2010343436)
            assert False
        except ValueError:
            assert True
        
        try:
            self._service.update(10,"Laur",2010343436222)
            assert False
        except ValueError:
            assert True
            
        try:
            self._service.remove(10,"Lindsey",2010343436333)
            assert False
        except ValueError:
            assert True
    
        try:
            self._service.removeAll()
            assert True
        except ValueError:
            assert False
            
    
    
    
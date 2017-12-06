'''
Created on Nov 26, 2017

@author: Monica
'''
import unittest
from domain.customer import customer
class testCustomer(unittest.TestCase):

    def setUp(self):
        self.__id=1
        self.__name="Michael"
        self.__cnp=2981211334567

    def tearDown(self):
        pass
    
    def testCustomer(self):
        self._customer=customer(self.__id,self.__name,self.__cnp)
        self.assertEqual(self.__id, 1)
        self.assertEqual(self.__name,"Michael" )
        self.assertEqual(self.__cnp,2981211334567)
        self.assertEqual(self._customer,customer(self.__id,self.__name,self.__cnp))
    
    
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
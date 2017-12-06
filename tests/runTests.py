'''
Created on Nov 15, 2017

@author: Monica
'''
from tests.testsMovie import testMovie,testServiceM, testRepositoryM
from tests.testRent import testRepositoryR
from tests.testCustomer import testCustomer, testServiceC, testRepositoryC
def runTests():
    testMovie()
    testServiceM()
    testRepositoryM()
    testCustomer()
    testServiceC()
    testRepositoryC()
    testRepositoryR()
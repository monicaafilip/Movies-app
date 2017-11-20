'''
Created on Nov 15, 2017

@author: Monica
'''
from tests.testsMovie import testMovie,testControllerM, testRepositoryM
from tests.testCustomer import testCustomer, testRepositoryC
from tests.testCustomer import testControllerC
def runTests():
    testMovie()
    testControllerM()
    testRepositoryM()
    testCustomer()
    testControllerC()
    testRepositoryC()
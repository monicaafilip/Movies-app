'''
Created on Nov 12, 2017

@author: Monica
'''
from UI.ui import console
from controller.controllerM import moviesController
from repository.repoMovies import moviesRepository
from controller.controllerC import customersController
from repository.repoCustomers import customersRepository
from validator.validatorMovie import validatorMovie
from validator.validatorCustomer import validatorCustomer
from tests.runTests import runTests
def main():
    c=console(moviesController(moviesRepository(),validatorMovie()),customersController(customersRepository(),validatorCustomer()))
    c.interface()
    runTests()
main()

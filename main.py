'''
Created on Nov 12, 2017

@author: Monica
'''
from UI.ui import console
from service.serviceM import moviesService
from service.serviceC import customersService
from validator.validatorMovie import validatorMovie
from validator.validatorCustomer import validatorCustomer
#from tests.runTests import runTests
from repository.repository import repository
from service.serviceR import rentsService
from validator.validatorRent import validatorRent
from repository.fileRepository import fileRepository
from domain.movie import movie
from domain.customer import customer
import os
from service.serviceReports import serviceReports
from domain.rent import rent
def main():
    
    #runTests()
    typee=console.getTheTypeOfRepository()
    if typee=='in memory':
        moviesRepository=repository()
        customersRepository=repository()
        rentsRepository=repository()
    
    elif typee=='in file':
        scriptpath = os.path.dirname(__file__)
        fileNameM = os.path.join(scriptpath,"movies.txt")
        fileNameC = os.path.join(scriptpath,"customers.txt")
        fileNameR=os.path.join(scriptpath,"rents.txt")
        moviesRepository=fileRepository(fileNameM,movie.readFromStr,movie.writeToStr)
        customersRepository=fileRepository(fileNameC,customer.readFromStr,customer.writeToStr)
        rentsRepository=fileRepository(fileNameR,rent.readFromStr,rent.writeToStr)
        
    c=console(moviesService(moviesRepository,validatorMovie()),customersService(customersRepository,validatorCustomer()),rentsService(moviesRepository,customersRepository,rentsRepository,validatorRent()),serviceReports(rentsRepository,customersRepository,moviesRepository))
    
    c.interface()
   

main()



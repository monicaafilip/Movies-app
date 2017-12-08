'''
Created on Nov 13, 2017

@author: Monica
'''
from validator.validatorCommands import validatorCommandsException,\
    validatorCommands
from UI.rentsMenu import rentsMenu
from UI.reports import reports
from UI.moviesMenu import moviesMenu
from UI.customersMenu import customersMenu
class consoleExceptions(Exception):
    pass
class console:
    def __init__(self,srvMovie,srvCustomer,srvRent,srvRep):
        self.__serviceMovie=srvMovie
        self.__serviceCustomer=srvCustomer
        self.__serviceRent=srvRent
        self.__serviceReports=srvRep
        self.valid=validatorCommands()
    
    @staticmethod
    def getTheTypeOfRepository():
        '''
        asks the user what type of repository wants to use and return that type as a string
        out:'in file'
             or
            'in memory'
        '''
        while True:
            print("Hello! First choose the type of repository:")
            print("1.In memory")
            print("2.From file")
            cmd=input("Give the option:")
            try:
                validatorCommands().validate(cmd, 2)
            except validatorCommandsException as ex:
                print(ex)
            cmd=int(cmd)
            if cmd==1:
                return 'in memory'
            elif cmd==2:
                return 'in file'
                
        
    def interface(self):
        while True:
            print("\n=====Menu=====")
            print("1.Movies menu")
            print("2.Customers menu")
            print("3.Rents menu")
            print("4.Reports menu")
            print("0.Exit")
            cmd=input("Give a command:")
            try:
                self.valid.validate(cmd,4)
                com=int(cmd)
                if com==0:
                    return
                elif com==1:
                    moviesMenu(self.__serviceMovie,self.__serviceRent).show()
                elif com==2:
                    customersMenu(self.__serviceCustomer,self.__serviceRent).show()
                 
                elif com==3:
                    rentsMenu(self.__serviceRent).show()
                elif com==4:
                    reports(self.__serviceReports).show()
                    
                    
           
            except validatorCommandsException as ve:
                print(ve)
            

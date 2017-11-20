'''
Created on Nov 13, 2017

@author: Monica
'''
from UI.moviesMenu import moviesMenu
from UI.customersMenu import customersMenu
from validator.validatorCommands import validatorCommandsException,\
    validatorCommands
class consoleExceptions(Exception):
    pass
class console:
    def __init__(self,cMovie,cCustomer):
        self.__controllerMovie=cMovie
        self.__controllerCustomer=cCustomer
        self.valid=validatorCommands()
        
    def interface(self):
       
        while True:
            print("===Menu===")
            print("1.Movies menu")
            print("2.Customers menu")
            print("0.Exit")
            cmd=input("Give a command:")
            try:
                self.valid.validate(cmd,2)
                com=int(cmd)
                if com==0:
                    return
                elif com==1:
                    moviesMenu(self.__controllerMovie).show()
                elif com==2:
                    customersMenu(self.__controllerCustomer).show()
            except validatorCommandsException as ve:
                print(ve)
            

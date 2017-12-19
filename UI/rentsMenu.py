'''
Created on Nov 22, 2017

@author: Monica
'''
from validator.validatorCommands import validatorCommands,\
    validatorCommandsException
from repository.repository import repositoryExceptions
from validator.validatorRent import validatorRentExceptions, validatorRent
from validator.validatorMovie import validatorMovie, validatorMovieExceptions
from validator.validatorCustomer import validatorCustomer,\
    validatorCustomerExceptions

class rentsMenu:
    def __init__(self,srvRent):
        self.__serviceRent=srvRent
        self.valid=validatorCommands()
        self.validM=validatorMovie()
        self.validC=validatorCustomer()
        self.validR=validatorRent()
    def addRent(self):
        '''
        rents a movie to a customer
        '''
        idR=input("Give the rent id:")
        idM=input("Give the movie id:")
        idC=input("Give the customer id:")
        try:
            try:
                self.validM.validateId(idM)
                self.validC.validateId(idC)
                self.validR.validate(idR)
                idR=int(idR)
                idM=int(idM)
                idC=int(idC)
            
                r=self.__serviceRent.createRent(idR,idM,idC)
                print(" Rent " + str(r.getId()) + " added succesfully!\n")

            except validatorRentExceptions as ex:
                print(ex)
            except validatorMovieExceptions as ex:
                print (ex)
            except validatorCustomerExceptions as ex:
                print(ex)
        
        except repositoryExceptions as ex:
            print(ex)
        except validatorRentExceptions as ex:
            print(ex)
        except validatorCustomerExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def removeAllRents(self):
        '''removes all rents'''
        try:
            self.__serviceRent.removeAll()
            print("Rents removed succesfully!\n")
        except repositoryExceptions as ex:
            print(ex)
        except validatorRentExceptions as ex:
            print(ex)
            
    def findById(self):
        '''finds a rent by id'''
        idR=input("Give the id:")
        try:
            try:
                self.validR.validate(idR)
                idR=int(idR)
            except validatorRentExceptions as ex:
                print(ex)
            r=self.__serviceRent.find("id",idR)
            if len(r)==0:
                print("No rent found!\n")
            else:
                print("Rent found succesfully ! "+r.__str__())
        except repositoryExceptions as ex:
            print(ex)
        except validatorRentExceptions as ex:
            print(ex)
            
    def findByMovieId(self):
        '''finds a rent by a movie id'''
        idM=input("Give the movie id:")
        try:
            try:
                self.validM.validateId(idM)
                idM=int(idM)
            except validatorMovieExceptions as ex:
                print(ex)
            r=self.__serviceRent.find("idM",idM)
            if len(r)==0:
                print("No rent found!\n")
            else:
                print("Rent found succesfully ! "+r.__str__())
        except repositoryExceptions as ex:
            print(ex)
        except validatorRentExceptions as ex:
            print(ex)
    
    def findByCustomerId(self):
        '''finds a rent by a customer id'''
        idC=input("Give the customer id:")
        try:
            try:
                self.validC.validateId(idC)
                idC=int(idC)
            except validatorCustomerExceptions as ex:
                print(ex)
            r=self.__serviceRent.find("idC",idC)
            if len(r)==0:
                print("No rent found!\n")
            else:
                print("Rent found succesfully ! "+r.__str__())
        except repositoryExceptions as ex:
            print(ex)
        except validatorRentExceptions as ex:
            print(ex)
            
    def sortById(self):
        '''sorts the rents by id'''
        if self.__serviceRent.getNrRents()==0:
            print("The list has no rents!\n")
        else:
            rents=self.__serviceRent.sortBy("id")
            for i in rents:
                print(i.__str__())
            print("List sorted succesfully!\n")
            
    def showARent(self):
        '''shows a rent with an given id'''
        idR=input("Give the rent id:")
        try:
            self.validR.validate(idR)
            idR=int(idR)
            for i in self.__serviceRent.getAll():
                if int(i.getId())==idR:
                    print(i.__str__())
        except repositoryExceptions as ex:
            print(ex)
        except validatorRentExceptions as ex:
            print(ex)
            
    def showAllRents(self):
        '''shows all the rents'''
        printed=False
        for i in self.__serviceRent.getAll():
            print(i.__str__())
            printed=True
        if printed==False:
            print("There are't rents yet!\n")
            
    def populateRandom(self,limit):
        '''
        populate the repository with random elements
        '''
        while limit!=0:
            try:
                limit=self.__serviceRent.populateRandom(limit) 
                print("The repository was populated successfully!\n")
            except repositoryExceptions:
                print("The repository was populated successfully but with less rents!\n")
                break
        
    def show(self):
        while True:
            print("===Rents menu===")
            print("1.Add")
            print("2.Find")
            print("3.Show")
            print("4.Sort by id")
            print("5.Populate random")
            print("0.Exit")
            print()
            cmd=input("Give command:")
            try:
                self.valid.validate(cmd,5)
                com=int(cmd)
                if com==0:
                    return
                elif com==1:
                    self.addRent()
                elif com==2:
                    print("--Find menu--")
                    print("1.By id")
                    print("2.By movie id")
                    print("3.By customer id")
                    print("0.Exit")
                    print()
                    cmd=input("Give command:")
                    try:
                        self.valid.validate(cmd,3)
                        com=int(cmd)
                        if com==0:
                            break
                        elif com==1:
                            self.findById()
                        elif com==2:
                            self.findByMovieId()
                        elif com==3:
                            self.findByCustomerId()
                    except validatorCommandsException as ex:
                        print(ex)
                elif com==3:
                    print("--Show menu--")
                    print("1.Show a rent")
                    print("2.Show all rents")
                    print("0.Exit")
                    print()
                    cmd=input("Give command:")
                    try:
                        self.valid.validate(cmd,2)
                        com=int(cmd)
                        if com==0:
                            break
                        elif com==1:
                            self.showARent()
                        elif com==2:
                            self.showAllRents()
                    except validatorCommandsException as ex:
                        print(ex)
                elif com==4:
                    self.sortById()
                elif com==5:
                    try:
                        limit=int(input("Give the number of rents:"))
                        self.populateRandom(limit)
                    except ValueError:
                        print("The limit can't be string!\n")    
                    
            except validatorCommandsException as ex:
                print(ex)

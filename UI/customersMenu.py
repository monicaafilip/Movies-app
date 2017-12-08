'''
Created on Nov 13, 2017

@author: Monica
'''
from repository.repository import repositoryExceptions
from validator.validatorCustomer import validatorCustomerExceptions
from validator.validatorCommands import validatorCommands,\
    validatorCommandsException
class customersMenu:
    def __init__(self,srvCustomer,srvRent):
        self.__serviceCustomer=srvCustomer
        self.valid=validatorCommands()
        self.__serviceRent=srvRent
        
    def addCustomer(self):
        '''
        adds a customer
        '''
        idC=input("Give the id:")
        name=input("Give the name:")
        cnp=input("Give the cnp:")
        try:
            c=self.__serviceCustomer.createCustomer(idC,name,cnp)
            print(" Customer " + c.getName() + " added succesfully!\n")
        except repositoryExceptions as ex:
            print(ex)
        except validatorCustomerExceptions as ex:
            print(ex)
            
            
    def removeACustomer(self):
        '''
        removes a customer 
        '''
        idC=input("Give the id:")
        try:
            idC=int(idC)
            self.__serviceCustomer.remove(idC)
            self.__serviceRent.removeAfterKey("customer",idC)
            print("Customer removed succesfully!\n")
        except ValueError:
            print("The id must be integer!\n")
        except repositoryExceptions as ex:
            print(ex)
        except validatorCustomerExceptions as ex:
            print(ex)
            
    def removeAllCustomers(self):
        '''removes all customers from a customer'''
        try:
            self.__serviceCustomer.removeAll()
            print("Customers removed succesfully!\n")
        except repositoryExceptions as ex:
            print(ex)
        except validatorCustomerExceptions as ex:
            print(ex)
            
    def findById(self):
        '''finds a customer by id'''
        idC=input("Give the id:")
        try:
            c=self.__serviceCustomer.find("id",idC)
            if len(c)==0:
                print("No customer found!\n")
            else:
                print("Customer found succesfully! \n "+ c[0].__str__())
        except repositoryExceptions as ex:
            print(ex)
        except validatorCustomerExceptions as ex:
            print(ex)
            
    def findByName(self):
        '''finds customers by name'''
        name=input("Give the name:")
        try:
            c=self.__serviceCustomer.find("name",name)
            if len(c)==0:
                print("No customer found!\n")
            else:
                i=0
                while i<len(c):
                    print("Customer found succesfully! \n "+ c[i].__str__())
                    i+=1
        except repositoryExceptions as ex:
            print(ex)
        except validatorCustomerExceptions as ex:
            print(ex)
            
    def findByCnp(self):
        '''finds a customer by cnp'''
        cnp=input("Give the cnp:")
        try:
            c=self.__serviceCustomer.find("cnp",cnp)
            if len(c)==0:
                print("No customer found!\n")
            else:
                print("Customer found succesfully! "+c[0].__str__())
        except repositoryExceptions as ex:
            print(ex)
        except validatorCustomerExceptions as ex:
            print(ex)
            
    def sortById(self):
        '''sorts the customers by id'''
        if self.__serviceCustomer.getNrCustomers()==0:
            print("The list has no customers!\n")
        else:
            customers=self.__serviceCustomer.sortBy("id")
            for i in customers:
                print(i.__str__())
            print("List sorted succesfully!\n")
            
    def filterByName(self):
        '''
        prints the customers with a specified name
        '''
        name=input("Give the name:")
        try:
            c=self.__serviceCustomers.filterByName("name",name)
            if len(c)==0:
                print("No customers with this name found!\n")
            else:
                i=0
                while i<len(c):
                    print("Customer with the name "+name+" :"+c[i].__str__())
                i+=1
        except repositoryExceptions as ex:
            print(ex)
        except validatorCustomerExceptions as ex:
            print(ex)
            
    def updateCustomer(self):
        '''modifies a customer'''
        newId=input("Give the id:")
        newName=input("Give a new name:")
        newCnp=input("Give a new cnp:")
        try:
            self.__serviceCustomer.update(newId,newName,newCnp)
            print("Customer modified succesfully!")
        except repositoryExceptions as ex:
            print(ex)
        except validatorCustomerExceptions as ex:
            print(ex)
            
    def showACustomer(self):
        '''shows a customer with an given id'''
        try:
            self.findById()
        except repositoryExceptions as ex:
            print(ex)
        except validatorCustomerExceptions as ex:
            print(ex)
            
    def showAllCustomers(self):
        '''shows all the customers'''
        printed=False
        for i in self.__serviceCustomer.getAll():
            print(i.__str__())
            printed=True
        if printed==False:
            print("There are't customers yet!\n")
           
    def populateRandom(self,limit):
        '''
        populate the repository with random objects
        '''
        try:
            self.__serviceCustomer.populateRandom(limit) 
            print("The repository was populated successfully!\n")
        except repositoryExceptions as ex:
            print(ex)
    
    def show(self):
        while True:
            print("\n===Customers menu===")
            print("1.Add")
            print("2.Remove")
            print("3.Find")
            print("4.Update")
            print("5.Show")
            print("6.Sort by id")
            print("7.Filter by name")
            print("8.Populate random")
            print("0.Exit")
            print()
            cmd=input("Give command:")
            try:
                self.valid.validate(cmd,8)
                com=int(cmd)
                if com==0:
                    return
                elif com==1:
                    self.addCustomer()
                elif com==2:
                    print("\n--Remove menu--")
                    print("1.Remove a customer")
                    print("2.Remove all customers")
                    print("0.Exit")
                    print()
                    cmd=input("Give command:")
                    try:
                        self.valid.validate(cmd,2)
                        com=int(cmd)
                        if com==1:
                            self.removeACustomer()
                        elif com==2:
                            self.removeAllCustomers()
                        elif com==0:
                            break
                    except validatorCommandsException as ex:
                        print(ex)
                elif com==3:
                    print("\n--Find menu--")
                    print("1.By id")
                    print("2.By name")
                    print("3.By cnp")
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
                            self.findByName()
                        elif com==3:
                            self.findByCnp()
                    except validatorCommandsException as ex:
                        print(ex)
                elif com==4:
                    self.updateCustomer()
                elif com==5:
                    print("--Show menu--")
                    print("1.Show a customer")
                    print("2.Show all customers")
                    print()
                    cmd=input("Give command:")
                    try:
                        self.valid.validate(cmd,2)
                        com=int(cmd)
                        if com==0:
                            break
                        elif com==1:
                            self.showACustomer()
                        elif com==2:
                            self.showAllCustomers()
                    except validatorCommandsException as ex:
                        print(ex)
                elif com==6:
                    self.sortById()
                elif com==7:
                    self.filterByName()
                elif com==8:
                    try:
                        limit=int(input("Give the number of customers:"))
                        self.populateRandom(limit)
                    except ValueError:
                        print("The limit must be an integer number!\n")
            except validatorCommandsException as ex:
                print(ex)






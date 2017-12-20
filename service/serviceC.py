'''
Created on Nov 14, 2017

@author: Monica
'''
from domain.customer import customer
import random
class customersService:
    def __init__(self,repo,valid):
        '''
        initializes the customer
        in:    -> repo:repoCustomers
               -> valid:validatorCustomers
        '''
        self.__repository=repo
        self.__validator=valid
        
    def createCustomer(self,idC,name,cnp):
        '''
        creates a customer
        in:   ->idC:int unique
              ->name:string
              ->cnp:int
        out:the customer created
        '''
        c=customer(idC,name,cnp)
        self.__validator.validate(c)
        self.__repository.store(c)
        return c
    
    def update(self,idC,name,cnp):
        '''
        updates the informations of a customer 
        '''
        c=customer(idC,name,cnp)
        self.__validator.validate(c)
        self.__repository.modify(c)
    
    def remove(self,idC):
        '''
        removes a customer with an unique id:idC(in ->integer number)
        '''
        self.__repository.remove(idC)
    
    def removeAll(self):
        '''
        removes all movies
        '''
        self.__repository.clearList()
 
    def find(self,nameK,valueK):
        '''
        find customers with a specified key
        in:  ->nameK(the name of key):can be id/title/genre
             ->valueK(the value of key)
        out: the customer
        '''
        return self.__repository.find(nameK,valueK)
    
    def filterBy(self,nameK,valueK):
        '''
        find customers with a specified key whose value is a string
        in:  ->nameK(the name of key):can be name in this case
             ->valueK(the value of key)
        out: the movie
        '''
        allCustomers=self.__repository.getAll()
        filteredCustomers=[]
        for i in range(len(allCustomers)):
            if (nameK=="name" and allCustomers[i].getName()==valueK) :
                filteredCustomers.append(allCustomers[i])
        return filteredCustomers
       
    
    def sortBy(self,nameK):
        '''
        sorts the list of customers by a specified key
        in:nameK (the key)
        out:-
        '''
        if nameK=="id":
            return sorted(self.__repository.getAll(), key=lambda k:k.getId(),reverse=True)

    def get(self,idC):
        '''
        gets a movie
        in:the unique id (idC) -an integer number
        out:the customer
        '''
        return self.__repository.get(idC)
    
    def getAll(self):
        '''
        gets all the customers
        in:-
        out:the list of customers
        '''
        return self.__repository.getAll()
    
    def getNrCustomers(self):
        '''
        gets the number of customers
        in:-
        out:the number of customers
        '''
        return self.__repository.sizeOfList()
    
    
    def populateRandom(self,limit):
        while limit!=0:
            idC=random.randrange(1000)
            name=random.choices(["Ingrid","Camelia","Cosmin","Carmen","Filip","Tudor","Emi","Michael","Bella"])[0]
            cnp=random.randint(1000000000000,100000000000000)
            self.createCustomer(idC, name, cnp)
            limit-=1
        return limit

    def getAllId(self):
        '''
        get a list with integer element with all the customers id
        '''
        lst=[]
        for i in self.getAll():
            lst.append(int(i.getId()))
            
        return lst
'''
Created on Nov 13, 2017

@author: Monica
'''
class customersRepositoryExceptions(Exception):
    pass
class customersRepository:
    '''
    stores customers in memory
    '''
    def __init__(self):
        self.__customers={}
        
    def store(self,customer):
        '''
        stores a customer in memory if it does not exist yet,else raise an exception
        in:customer
        out:-
        '''
        if customer.getId() in self.__customers:
            raise customersRepositoryExceptions("This customer already exists! Give another id!")
        elif customer.getCnp() in self.__customers:
            raise customersRepositoryExceptions("This customer already exists! Give another cnp!")
        else:
            self.__customers[customer.getId()]=customer
            
    def clearList(self):
        '''
        remove all the customers
        '''
        if self.sizeOfList()!=0:
            self.__customers={}
        else:
            raise customersRepositoryExceptions("The list has no customers!\n")
        
    def modify(self,customer):
        '''
        modifies a customer that already exists,else raise an exception
        in:customer
        out:-
        '''
        for i in self.__customers.values():
            if i.getId()==customer.getId():
                self.__customers[customer.getId()]=customer
            else:
                raise customersRepositoryExceptions("This id does not exist in the movies list!")
    
    def sizeOfList(self):
        '''
        the numbers of customers
        in:-
        out:the numbers of customers (an integer number)
        '''
        return len(self.__customers)
    
    def remove(self,customer):
        '''
        removes a customer that exists,else raise an exception
        in:customer
        out:
        
        '''
        try:
            self.__customers.pop(customer)
        except KeyError:
            raise customersRepositoryExceptions("This customer does not exist in the customers list!")
    
    
    def find(self,nameK,valueK,index=0):
        '''
        finds all customers after a key
        in: ->nameK(the name of key):can be id/title/genre
            ->valueK(the value of key): the value of id/title/genre
            ->index: starts from 0 until the end of the customers list
        out: list of customers
        '''
        allCustomers=list(self.__customers.values())
        foundCustomers=[]
        for index in range(len(allCustomers)):
            if (nameK=='id' and allCustomers[index].getId()==valueK) or\
               (nameK=='name' and allCustomers[index].getName()==valueK) or\
               (nameK=='cnp' and allCustomers[index].getCnp()==valueK):
                foundCustomers.append(allCustomers[index])
                
        return foundCustomers
        
    
    def get(self,idC):
        '''
        gets the customer
        in: ->the unique id (an integer number)
        out:the customer or the exception when the id does not exist in the list
        '''
        try:
            return self.__customers[idC]
        except KeyError:
            raise customersRepositoryExceptions("The id does not exist!\n")
        
    def getAll(self):
        '''
        gets all the movies 
        in:-
        out: the list of movies
         '''
        return list(self.__customers.values())
            

        
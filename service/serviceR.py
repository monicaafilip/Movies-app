'''
Created on Nov 22, 2017

@author: Monica
'''
from domain.rent import rent
import random
class rentsService:
    def __init__(self,repoM,repoC,repoR,valid):
        '''
        initializes a rent
        in:    ->repoM:repoMovies
               -> repoC:repoCustomers
               ->repoR:repoRents
               ->validator
        '''
        self.__repositoryM=repoM
        self.__repositoryC=repoC
        self.__repositoryR=repoR
        self.__validator=valid
        
    def createRent(self,idR,idM,idC):
        '''
        creates a rent
        in:   ->idR:(int unique) the rent id
              ->idM:(int unique) the movie id
              ->idC:(int unique) the customer id
        out:the customer created
        '''
        r=rent(idR,idM,idC)
        self.__validator.validate(idR)
        cust=self.__repositoryC.getAll()
        mov=self.__repositoryM.getAll()
        self.__validator.validateMId(idM,mov)
        self.__validator.validateCId(idC,cust)
        self.__repositoryR.store(r)
        return r

    def update(self,idR,idM,idC,status):
        '''
        updates a customer info
        parameters :  ->idR :unique rent id (integer no)
                      ->idM :unique movie id(integer no)
                      ->idC :unique customer id (integer no)
                      ->status :rent status ("rented"/"returned")
        '''
        r=rent(idR,idM,idC,status)
        self.__validator.validate(r)
        self.__repositoryR.modify(r)
        
    def returnMovie(self,idR):
        '''
        returns a movie from a customer
        idR :unique rent id (integer no)
        '''
        self.__repositoryR.returnMovie(idR)
        
    

    def remove(self,idR):
        '''
        removes a rent with an unique id:idR(in ->integer number)
        '''
        self.__repositoryR.remove(idR)
    
    def removeAll(self):
        '''
        removes all rents
        '''
        self.__repositoryR.clearList()
 
    def find(self,nameK,valueK):
        '''
        find rents with a specified key
        in:  ->nameK(the name of key):can be idR,idM,idC
             ->valueK(the value of key)
        out: the rent
        '''
        return self.__repositoryR.find(nameK,valueK)
    
    def sortBy(self,nameK):
        '''
        sorts the list of customers by a specified key
        in:nameK (the key)
        out:-
        '''
        if nameK=="id":
            return sorted(self.__repositoryR.getAll(), key=lambda k:k.getId(),reverse=True)

    def get(self,idR):
        '''
        gets a rent
        in:the unique id (idR) -an integer number
        out:the rent
        '''
        return self.__repositoryR.get(idR)
    
    def getAll(self):
        '''
        gets all the rents
        in:-
        out:the list of rents
        '''
        return self.__repositoryR.getAll()
    
    def getNrRents(self):
        '''
        gets the number of rents
        in:-
        out:the number of rents
        '''
        return self.__repositoryR.sizeOfList()
    
    def randomMovies(self):
        '''
        get a list with integer elements with all the movies id
        '''
        lst=[]
        for i in self.__repositoryM.getAll():
            lst.append(int(i.getId()))
        return lst
    
    def randomCustomer(self):
        '''
        get a list with integer elements with all the customers id
        '''
        lst=[]
        for i in self.__repositoryC.getAll():
            lst.append(int(i.getId()))
        return lst
    def populateRandom(self,limit):
        if limit<len(self.randomMovies()) and limit<len(self.randomCustomer()):
            while limit!=0:
                idR=random.randrange(1000)
                idM=random.choices(self.randomMovies())[0]
                idC=random.choices(self.randomCustomer())[0]
                rent=self.createRent(idR, idM, idC)
                limit-=1
        else:
            limit=-1
        return limit
            
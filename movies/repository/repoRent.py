'''
Created on Nov 20, 2017

@author: Monica
'''
class rentsRepositoryExceptions(Exception):
        pass
        
class rentRepository:
    '''
    stores rents in memory
    '''
    def __init__(self):
        self.__rents={}
        
    def store(self,rent):
        '''
        stores a rent in memory if it does not exist yet,else raise an exception
        in:rent
        out:-
        '''
        if rent.getId() in self.__rents:
            raise rentsRepositoryExceptions("This rent already exists! Give another id!")
        else:
            self.__rents[rent.getId()]=rent
            
    def clearList(self):
        '''
        remove all the rents
        '''
        if self.sizeOfList()!=0:
            self.__rents={}
        else:
            raise rentsRepositoryExceptions("The list has no rents!\n")
    def modify(self,rent):
        '''
        modifies a rent that already exists,else raise an exception
        in:rent
        out:-
        '''        
        for i in self.__rents.values():
            if i.getId()==rent.getId():
                self.__rents[rent.getId()]=rent
            else:
                raise rentsRepositoryExceptions("This id does not exist in the rents list!")
    
    def sizeOfList(self):
        '''
        the numbers of rents
        in:-
        out:the numbers of rents (an integer number)
        '''
        return len(self.__rents)
    
    def remove(self,idR):
        '''
        removes a rent that exists,else raise an exception
        in:rent
        out:
        
        '''
        try:
            self.__rents.pop(idR)
        except KeyError:
            raise rentsRepositoryExceptions("This rent does not exist in the rents list!")
        
    def returnMovie(self,idR):
        '''
        returns a movie to the store
        in:the rent's id
        out:-
        '''
        try:
            self.__rents[idR].returnMovie()
        except:
            raise rentsRepositoryExceptions("The id does not exist!\n")

    def get(self,idR):
        '''
        gets the rent 
        in: ->the unique id (an integer number)
        out:the rent or the exception when the id does not exist in the list
        '''
        try:
            return self.__rents[idR]
        except KeyError:
            raise rentsRepositoryExceptions("The id does not exist!\n")
        
    def getAll(self):
        '''
        gets all the rents 
        in:-
        out: the list of rents
         '''
        return list(self.__rents.values())
            
        

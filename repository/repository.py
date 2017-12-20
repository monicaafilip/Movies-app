'''
Created on Nov 13, 2017

@author: Monica'''

class repositoryExceptions(Exception):
        pass
        
class repository:
    '''
    stores elements in memory
    '''
    def __init__(self):
        self._elems={}
        
    def store(self,elem):
        '''
        stores an element in memory if it does not exist yet,else raise an exception
        in:elem
        out:-
        '''
    
        if elem.getId() in self._elems:
            raise repositoryExceptions("This id already exists!\n")
        else:
            self._elems[elem.getId()]=elem
      
    def clearList(self):
        '''
        remove all the elems
        '''
        if self.sizeOfList()!=0:
            self._elems={}
        else:
            raise repositoryExceptions("The list has no elements!\n")
    
    def modify(self,elem):
        '''
        modifies an element that already exists,else raise an exception
        in:elem
        out:-
        '''        
        if elem.getId() in self._elems.keys():
            self._elems[elem.getId()]=elem
        else:
            raise repositoryExceptions("This id does not exist in the elements list!")

   
    def sizeOfList(self):
        '''
        the numbers of elements
        in:-
        out:the numbers of elements (an integer number)
        '''
        return len(self._elems)
    
    def remove(self,idd):
        '''
        removes an element that exists,else raise an exception
        in:elem
        out:
        
        '''
        try:
            self._elems.pop(idd)
        except KeyError:
            raise repositoryExceptions("This id does not exist in the list!")
    
    def find(self,nameK,valueK,index=0):
        '''
        finds all elements after a key
        in: ->nameK(the name of key)
            ->valueK(the value of the key)
            ->index: starts from 0 until the end of the elements list
        out: list of elements
        '''
        '''
        ----the complexity of this algorithm---
        best case:when the found element is on the first position
            t(n)=1
        worst case:when the found element is on the last position
            t(n)=n
        =>O(n)=n
        '''
        allElems=list(self._elems.values())
        foundElems=[]
        for index in range(len(allElems)):
            if (nameK=='id' and allElems[index].getId()==valueK) or\
               (nameK=='title' and allElems[index].getTitle()==valueK) or\
               (nameK=='genre' and allElems[index].getGenre()==valueK) or\
               (nameK=='name' and allElems[index].getName()==valueK) or\
               (nameK=='cnp' and allElems[index].getCnp()==valueK)or\
               (nameK=='idM' and allElems[index].getMovie()==valueK)or\
               (nameK=='idC' and allElems[index].getCustomer()==valueK):
                foundElems.append(allElems[index])
                
        return foundElems

    def findRec(self,nameK,valueK,lst,found):
        '''
        finds an element by a given field
        in: ->nameK(the name of key)
            ->valueK(the value of the key)
            ->index: starts from 0 until the end of the elements list
        out: the element or the exception
        '''
        if lst==[] and len(found)!=0:
            return found
        elif lst==[]:
            raise repositoryExceptions("It doesn't exist!\n")
        elif ( (nameK=="id" and lst[0].getId()==valueK) or\
                              (nameK=='title' and lst[0].getTitle()==valueK) or\
                              (nameK=='genre' and lst[0].getGenre()==valueK) or\
                              (nameK=='name' and lst[0].getName()==valueK) or\
                              (nameK=='cnp' and lst[0].getCnp()==valueK)or\
                              (nameK=='idM' and lst[0].getMovie()==valueK)or\
                              (nameK=='idC' and lst[0].getCustomer()==valueK)):
            found.append(lst[0])
            return self.findRec(nameK,valueK,lst[1:],found)
        else:
            return self.findRec(nameK,valueK,lst[1:],found)
            
        
    def get(self,idd):
        '''
        gets the elements
        in: ->the unique id (an integer number)
        out:the element or the exception when the id does not exist in the list
        '''
        try:
            return self._elems[idd]
        except KeyError:
            raise repositoryExceptions("The id does not exist!\n")
        
    def getAll(self):
        '''
        gets all the elements 
        in:-
        out: the list of elements
         '''
        return list(self._elems.values())
            
        

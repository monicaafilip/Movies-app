'''
Created on Dec 5, 2017

@author: Monica
'''
from domain.rentDTO import rentDTO
class serviceReports:
    def __init__(self,repoR,repoC,repoM):
        self.__repositoryR = repoR
        self.__repositoryC = repoC
        self.__repositoryM = repoM
    def createTheDTOList(self):
        '''
        creates an objectDTO list for all the renters 
        '''
        rents=self.__repositoryR.getAll()
        cust=self.__repositoryC.getAll()
        movies=self.__repositoryM.getAll()
        lst=[]
        obj=rentDTO(0,0,"",0,"",0)
        for i in rents:
            count=0
            obj.set_idR(i.getId())
            obj.set_idM(i.getMovie())
            obj.set_idC(i.getCustomer())
            for j in cust:
                if i.getCustomer()==int(j.getId()):
                    obj.set_custName(j.getName())
                    for k in movies:
                        if i.getMovie()==int(k.getId()):
                            obj.set_movName(k.getTitle())
                            count+=1
                obj.set_noRents(count)            
                break
            lst.append(obj)
        return lst
                
                    
    def getListsOfCustomersWithRentersByName(self):
        '''
        gets a list of customers who has movies rented
        the list contains all the properties for a rentDTO object
       '''
        lst=self.createTheDTOList()
        return sorted(lst, key=lambda k:k.get_custName())
    
    def getListOfRentersAscendingByNoMovies(self):
        '''
        gets the list of renters ascending by the no of rented movies
        the list contains all the properties for a rentDTO object
        '''
        renters=self.createTheDTOList()
        return sorted(renters,key=lambda k:k.get_noRents())
        
    def mostRentedMovies(self):
        '''
        return a list with the most rented movies,those one with 
        the biggest no of renters and the number of the most rented movies
        '''
        renters=self.createTheDTOList()
        noMax=0
        for i in range(len(renters)):
            if int(renters[i].get_noRents())>noMax:
                noMax=int(renters[i].get_noRents())
                
        lst=[]
        for i in renters:
            if int(i.get_noRents())==noMax:
                lst.append(i.get_movName())
            
        return noMax,lst
                 
    def top30(self):
        '''
        get a list of rentDTO objects with those renters
        who are in 30% renters with the most rented movies 
        '''
        renters=self.createTheDTOList()
        top=0,3*len(renters)
        keep=[]
        for i in renters:
            if i.get_noRents()==top:
                keep.append(i)
        
        return keep
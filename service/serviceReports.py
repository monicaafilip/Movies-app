'''
Created on Dec 5, 2017

@author: Monica
'''
from domain.rentersName import rentersName
from domain.mostRentedMovies import rentedMovies
from domain.topR import topR
class serviceReports:
    def __init__(self,repoR,repoC,repoM):
        self.__repositoryR = repoR
        self.__repositoryC = repoC
        self.__repositoryM = repoM
              
    def getListOfRentersAndNoRents(self):
        '''
        get a list of rentersName objects
        '''
        rents=self.__repositoryR.getAll()
        cust=self.__repositoryC.getAll()
        lst=[]
        
        for i in range(len(rents)):
            obj=rentersName("","")
            count=0
            for j in cust:
                if j.getId()==rents[i].getCustomer():
                    obj.set_nameCustomer(j.getName())
                    for k in rents:
                        if k.getCustomer()==j.getId():
                            count+=1
                    break
            obj.set_noRents(count)
            exist=False
            l=0
            while l<len(lst) and exist==False:
                if lst[l].get_nameCustomer()==obj.get_nameCustomer():
                    exist=True  
                l+=1 
            if exist==False:
                lst.append(obj)
        return lst
      
    def getListsOfCustomersWithRentersByName(self):
        '''
        gets a list of customers who has movies rented
        the list contains all the properties for a rentersName object
        '''
        
        lst=self.getListOfRentersAndNoRents()
        lst =sorted(lst,key=lambda k:k.get_nameCustomer())
        return lst
            
    def getListOfRentersAscendingByNoMovies(self):
        '''
        gets the list of renters ascending by the no of rented movies
        the list contains all the properties for a rentDTO object
        '''
        renters=self.getListOfRentersAndNoRents()
        return sorted(renters,key=lambda k:k.get_noRents())
        
    def getListOfRentedMovies(self):
        '''
        gets a list of rented movies and their no of rents
        '''
        rents=self.__repositoryR.getAll()
        movies=self.__repositoryM.getAll()
        lst=[]
        for i in range(len(rents)):
            obj=rentedMovies("","")
            count=0
            for j in movies:
                if j.getId()==rents[i].getMovie():
                    obj.set_title(j.getTitle())
                    for k in rents:
                        if k.getMovie()==j.getId():
                            count+=1
                            break
            obj.set_noRents(count)
            exist=False
            l=0
            while l<len(lst) and exist==False:
                if lst[l].get_title()==obj.get_title():
                    exist=True  
                l+=1 
            if exist==False:
                lst.append(obj)
        return lst
        
    def mostRentedMovies(self):
        '''
        return a list with the most rented movies,those one with 
        the biggest no of renters and the number of the most rented movies
        '''
        movies=self.getListOfRentedMovies()
        noMax=0
        for i in range(len(movies)):
            if int(movies[i].get_noRents())>noMax:
                noMax=int(movies[i].get_noRents())
                
        lst=[]
        for i in movies:
            if int(i.get_noRents())==noMax:
                lst.append(i.get_title())
            
        return noMax,lst
    
    def getListOfMostRented(self):
        '''
        gets a list of top30renters object which contains the
        customers for all the most rented movies
        '''          
        movies=self.__repositoryM.getAll()
        noMax,mostRented=self.mostRentedMovies()
        lst=[]
        obj=topR("","",0)
        for i in mostRented:
            obj=topR("","",0)
            obj.set_titleM(i)
            for j in movies:
                if j.getTitle()==i:
                    for k in self.__repositoryR.getAll():
                        if j.getId()==k.getMovie():
                            for l in self.__repositoryC.getAll():
                                if l.getId()==k.getCustomer():
                                    obj.set_nameC(l.getName())
                                    break
                            break
                        break
            for ii in range(len(lst)):
                if lst[ii].get_nameC()==obj.get_nameC():
                    obj.set_noRents(obj.get_noRents()+1)
                
            lst.append(obj)
        return lst
    def top30(self):
        '''
        get a list of rentDTO objects with those renters
        who are in 30% renters with the most rented movies 
       '''
        lst=self.getListOfMostRented()
        lst=sorted(lst,key=lambda k:k.get_noRents(),reverse=True)
        top=int(0.3*len(lst))
        i=0
        keep=[]
        if top!=0:
            keep=lst[0:top]
        return keep
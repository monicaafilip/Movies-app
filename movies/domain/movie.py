'''
Created on Nov 13, 2017

@author: Monica
'''
class movie:
    def __init__(self,idd,title,genre,description):
        self.__id=idd
        self.__title=title
        self.__description=description
        self.__genre=genre
    
    def getId(self):
        return self.__id
    
    def setId(self,newId):
        self.__id=newId
        
    def getTitle(self):
        return self.__title
    
    def setTitle(self,newTitle):
        self.__title=newTitle
        
    def getDescription(self):
        return self.__description
    
    def setDescription(self,newDescr):
        self.__description=newDescr
        
    def getGenre(self):
        return self.__genre
    
    def setGenre(self,newGenre):
        self.__genre=newGenre
    
    def __lt__(self,other):
        return self.__id<other.__id
    def __eq__(self,other):
        return self.__id==other.__id and self.__title==other.__title and self.__genre==other.__genre and self.__description==other.__description
   
    def __str__(self):
        return " Movie "+self.__id+" "+self.__title +" "+self.__genre+" "+self.__description

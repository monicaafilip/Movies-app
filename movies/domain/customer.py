'''
Created on Nov 13, 2017

@author: Monica
'''
        
class customer:
    def __init__(self,idd,name,cnp):
        self.__id=idd
        self.__name=name
        self.__cnp=cnp
    
    def getId(self):
        return self.__id
    
    def setId(self,newId):
        self.__id=newId
        
    def getName(self):
        return self.__name
    
    def setName(self,newName):
        self.__name=newName
        
    def getCnp(self):
        return self.__cnp
    
    def setCnp(self,newCnp):
        self.__cnp=newCnp
    
    def __eq__(self,other):
        return self.__id==other.__id and self.__name==other.__name and self.__cnp==other.__cnp
   
    
    def __str__(self):
        return "Customer "+self.__id+" "+self.__name+" "+self.__cnp

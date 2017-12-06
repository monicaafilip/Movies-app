'''
Created on Nov 20, 2017

@author: Monica
'''
class rent:
    def __init__(self,idR,movie,customer):
        self.__id=idR
        self.__movie=movie
        self.__customer=customer
        self.__status="rented"

    def getId(self):
        return self.__id


    def getMovie(self):
        return self.__movie


    def getCustomer(self):
        return self.__customer


    def getStatus(self):
        return self.__status


    def setId(self, value):
        self.__id = value


    def setMovie(self, value):
        self.__movie = value


    def setCustomer(self, value):
        self.__customer = value

    def returnMovie(self):
        self.__status="returned"
        
    def __eq__(self,other):
        return isinstance(other, self.__class__) and self.__id==other.__id and self.__customer==other.__customer and self.__movie==other.__movie and self.__status==other.__status
    
    def __str__(self):
        return " Rent "+str(self.__id)+" "+str(self.__movie) +" "+str(self.__customer)

    
    @staticmethod
    def readFromStr(line):
        words=line.split(" ")
        return rent(int(words[0]),words[1],words[2])
    
    @staticmethod
    def writeToStr(rent):
        return str(rent.getId())+" "+str(rent.getMovie())+" "+str(rent.getCustomer())
    
    
    
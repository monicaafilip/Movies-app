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
        
    
    
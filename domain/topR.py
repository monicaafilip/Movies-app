'''
Created on Dec 6, 2017

@author: Monica
'''
class topR:
    def __init__(self,nameC,titleM,noRents):
        '''
        in:    ->nameC:the customer name
               ->titleM:the movie title
               ->noRents:the no rents of movies from a customer
        '''
        self.__nameC = nameC
        self.__titleM = titleM
        self.__noRents = noRents

    def get_nameC(self):
        return self.__nameC


    def get_titleM(self):
        return self.__titleM


    def get_noRents(self):
        return self.__noRents


    def set_nameC(self, value):
        self.__nameC = value


    def set_titleM(self, value):
        self.__titleM = value


    def set_noRents(self, value):
        self.__noRents = value

    def __eq__(self,ot):
        return isinstance(other,__class__) and other.__nameC==self.__nameC and self.__titleM==other.__titleM and self.__noRents==other.__noRents

    def __str__(self):
        return self.__nameC+" "+" with no of rents:"+str(self.__noRents)
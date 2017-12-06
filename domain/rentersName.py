'''
Created on Dec 6, 2017

@author: Monica
'''
class rentersName:
    '''
    keeps object which have only the name of renters and the number of rents
    '''
    def __init__(self,nameCustomer,noRents):
        self.__nameCustomer = nameCustomer
        self.__noRents = noRents

    def get_nameCustomer(self):
        return self.__nameCustomer


    def get_noRents(self):
        return self.__noRents


    def set_nameCustomer(self, value):
        self.__nameCustomer = value


    def set_noRents(self, value):
        self.__noRents = value
    
    def __eq__(self,other):
        return isinstance(other,__class__) and self.__nameCustomer==other.__nameCustomer and self.__noRents==other.__noRents

    def __str__(self):
        return self.__nameCustomer+" with "+str(self.get_noRents())+" rents."
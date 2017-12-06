'''
Created on Dec 6, 2017

@author: Monica
'''
class rentedMovies:
    def __init__(self,title,noRents):
        self.__title = title
        self.__noRents = noRents

    def get_title(self):
        return self.__title


    def get_noRents(self):
        return self.__noRents


    def set_title(self, value):
        self.__title = value


    def set_noRents(self, value):
        self.__noRents = value

    def __eq__(self,other):
        return isinstance(other,__class__) and self.__title==other.__title and self.__noRents==other.__noRents

    def __str__(self):
        return self.__title+" with "+str(self.get_noRents())+" rents."


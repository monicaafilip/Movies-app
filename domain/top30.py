'''
Created on Dec 6, 2017

@author: Monica
'''
class top30Renters:
    def __init__(self,name,movie):
        self.__name = name
        self.__movie=movie

    def get_name(self):
        return self.__name

    def set_name(self, value):
        self.__name = value
        
    def get_movie(self):
        return self.__movie

    def set_movie(self, value):
        self.__movie = value
        
    def __str__(self):
        return self.__name +" with the movie:"+self.__movie


'''
Created on Dec 6, 2017

@author: Monica
'''
class top30Renters:
    def __init__(self,name,noRents):
        self.__name = name
        self.__noRents = noRents

    def get_name(self):
        return self.__name


    def get_noRents(self):
        return self.__noRents


    def set_name(self, value):
        self.__name = value


    def set_noRents(self, value):
        self.__noRents = value

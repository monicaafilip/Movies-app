'''
Created on Nov 27, 2017

@author: Monica
'''
class rentDTO:
    def __init__(self,idR,idC,custName,idM,movName,noRents):  
        '''
        initializes the object with:
            ->an unique id:idR (integer no)
            ->the customer id :idC (integer no)
            ->the name of the customer:custName (string no)
            ->the movie id:idM (integer no)
            ->the of the movie:movName (string no)
            ->the number of rents:noRents (integer no)
        '''
        self.__idR = idR
        self.__idC = idC
        self.__custName = custName
        self.__idM = idM
        self.__movName = movName
        self.__noRents = noRents
        self.__status="rented"

    def get_idR(self):
        return self.__idR


    def get_idC(self):
        return self.__idC


    def get_custName(self):
        return self.__custName


    def get_idM(self):
        return self.__idM


    def get_movName(self):
        return self.__movName


    def get_noRents(self):
        return self.__noRents


    def get_status(self):
        return self.__status


    def set_idR(self, value):
        self.__idR = value


    def set_idC(self, value):
        self.__idC = value


    def set_custName(self, value):
        self.__custName = value


    def set_idM(self, value):
        self.__idM = value


    def set_movName(self, value):
        self.__movName = value


    def set_noRents(self, value):
        self.__noRents = value


    def set_status(self, value):
        self.__status = value


    
    def __str__(self):
        return "Identifier :"+str(self.__idR)+";customer id:"+str(self.__idC)+" with the name:"+self.__custName+";movie id: "+str(self.__idM)+" with the title:"+self.__movName+ "and the no of rents:"+str(self.__noRents) 
    
    
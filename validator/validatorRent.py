'''
Created on Nov 22, 2017

@author: Monica
'''
class validatorRentExceptions(Exception):
    pass

class validatorRent:
    def validate(self,idR):
        errors=[]
        if type(idR)!=int:
            try:
                i=int(idR)
                if i<0:
                    errors.append("The id cannot be negative!\n")
            except: 
                errors.append("The id cannot be string!\n")
        if len(errors)>0:
            raise validatorRentExceptions(errors)
        
    def validateMId(self,idM,lstMov):
        '''
        validates the movie id to be sure that it is in the movie list
        '''
        done=False
        for i in range(len(lstMov)):
            if int(lstMov[i].getId())==idM:
                done=True
            
        if done==False:
            raise validatorRentExceptions("The movie id does not exist!\n")
        
    def validateCId(self,idC,lstCust):
        '''
        validates the customer id to be sure that it is in the customer list
        '''
        done=False
        for i in range(len(lstCust)):
            if int(lstCust[i].getId())==idC:
                done=True
            
        if done==False:
            raise validatorRentExceptions("The customer id does not exist!\n")
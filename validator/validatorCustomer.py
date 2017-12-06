'''
Created on Nov 14, 2017

@author: Monica
'''
class validatorCustomerExceptions(Exception):
    pass

class validatorCustomer:
    def validateId(self,idC):
        errors=[]
        if type(idC)!=int:
            try:
                idd=int(idC)
                if idd<0:
                    errors.append("The id cannot be negative!\n")
            except: 
                errors.append("The id cannot be string!\n")
        if len(errors):
            raise validatorCustomerExceptions(errors)
        
    def validateName(self,name):
        if name=="":
            raise validatorCustomerExceptions("The name cannot be empty!\n")
        
    def validateCnp(self,cnp):
        errors=[]
        if type(cnp)!=int:
            try:
                cnpp=int(cnp)
                if cnpp<1000000000000 or cnpp>9999999999999:
                    errors.append("The cnp must have 13 digits!\n")
                if cnpp<0:
                    errors.append("The cnp must be an integer positive number") 
            except:
                errors.appednd("The cnp cannot be string!\n")
        if len(errors):
            raise validatorCustomerExceptions(errors)
        
    def validate(self,cust):
        self.validateId(cust.getId())
        self.validateName(cust.getName())
        self.validateCnp(cust.getCnp())

'''
Created on Nov 14, 2017

@author: Monica
'''
class validatorCommandsException(Exception):
    pass

class validatorCommands:
    def validate(self,cmd,valMax):
        errors=[]
        if type(cmd)!=int:
            try:
                c=int(cmd)
                if c<0 or c>valMax:
                    errors.append("The command does not exist!\n")
            except :
                errors.append("The command cannot be string!\n")
       
        if cmd=="":
            errors.append("The command cannot be empty!\n")
       
        if len(errors)>0:
            raise validatorCommandsException(errors)
        
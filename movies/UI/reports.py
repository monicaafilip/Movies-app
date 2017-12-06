'''
Created on Nov 27, 2017

@author: Monica
'''
from validator.validatorCommands import validatorCommands,\
    validatorCommandsException
class reports:
    def __init__(self,reports):
        self.__srvReports=reports
        self.valid=validatorCommands()
        
    def sortedListRentersByName(self):
        '''
        sorts the list of renters by name
        return a sorted list with the renters
        '''
        return self.__srvReports.getListsOfCustomersWithRentersByName()
    
    def sortedListRentersByNoMovies(self):
        '''
        sorts the list of renters by the no of rents
        return a sorted list with the renters
        '''
        return self.__srvReports.getListOfRentersAscendingByNoMovies()
    
    def theMostRentedMovies(self):
        '''
        return the no of the most rented movies and
        a list with those movies,those one with the biggest no of renters
        '''
        return self.__srvReports.mostRentedMovies()
        
    def top30(self):
        '''
        get first 30% of renters which have the most rented movies
        '''
        return self.__srvReports.top30()
    
    def show(self):
        while True:
            print("===Reports menu===")
            print("1.The list of renters sorted ascending by name of customer")
            print("2.The list of renters sorted ascending by the number of rented movies")
            print("3.The most rented movies")
            print("4.Top 30 % renters with the most rented movies")
            print("0.Back\n")
            cmd=input("Give the command:")
            try:
                self.valid.validate(cmd, 4)
                cmd=int(cmd)
                if cmd==0:
                    break
                elif cmd==1:
                    lst=self.sortedListRentersByName()
                    if len(lst)==0:
                        print("There aren't renters yet!\n")
                    else:
                        for i in range(len(lst)):
                            print(lst[i].__str__())
                elif cmd==2:
                    lst=self.sortedListRentersByNoMovies()
                    if len(lst)==0:
                        print("There aren't renters yet!\n")
                    else:
                        for i in range(len(lst)):
                            print(lst[i].__str__())
                elif cmd==3:
                    noMax,lst=self.theMostRentedMovies()
                    if len(lst)==0:
                        print("There aren't renters yet!\n")
                    else:
                        print("The biggest no of rents is :"+str(noMax)+" and these are the movies:")
                        for i in range(len(lst)):
                            print(lst[i]+" ")
                        
                elif cmd==4:
                    renters=self.top30()
                    if len(renters)==0:
                        print("There aren't renters yet!\n")
                    else:
                        print("Top 30%:")
                        for i in renters:
                            print(i.__str__())
                            
            except validatorCommandsException as ex:
                print(ex)
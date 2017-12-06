'''
Created on Nov 27, 2017

@author: Monica
'''
from repository.repository import repository
class fileRepository(repository):
    '''
    stores elements into a file
    '''
    
    def __init__(self,fileName,readFromStr,writeToStr):
        repository.__init__(self)
        self._fileName=fileName
        self._readFromStr=readFromStr
        self._writeToStr=writeToStr
        self.loadFromFile()
        
    def loadFromFile(self):
        '''
        load all the lines from a file and put them in the elements list
        '''
        with open(self._fileName,"r") as f:
            for line in f.readlines():
                line=line.strip()
                if len(line)>0:
                    obj=self._readFromStr(line)
                    self._elems[-1]=obj
    
    def saveToFile(self):
        '''
        save the objects from the elements list in the file
        changed into string
        '''
        with open(self._fileName,"w") as f:
            for obj in self._elems:
                line=self._writeToStr(obj)
                f.write(line+"\n")
                
    def append(self,elem):
        '''
        append a line to the file
        '''
        with open(self._fileName,"a") as f:
            line=self._writeToStr(elem)
            f.write(line+"\n")
            
    def store(self,elem):
        '''
        stores the element in file
        '''
        repository.store(self, elem)
        self.append(elem)
        
    def clearList(self):
        '''
        removes all the elements
        '''
        repository.clearList(self)
        self.saveToFile()
        
    def modify(self, elem):
        '''
        modifies an element that already exists,else raise an exception
        in:elem
        out:-
        '''  
        repository.modify(self, elem)
        self.saveToFile()
        
    def remove(self, idd):
        '''
        removes an element with a given id
        '''
        repository.remove(self, idd)
        self.saveToFile()

'''
Created on Nov 14, 2017

@author: Monica
'''

class validatorMovieExceptions(Exception):
    pass

class validatorMovie:
    def validateId(self,idM):
        errors=[]
        if type(idM)!=int:
            try:
                i=int(idM)
                if i<0:
                    errors.append("The id cannot be negative!\n")
            except: 
                errors.append("The id cannot be string!\n")
        if len(errors)>0:
            raise validatorMovieExceptions(errors)
    def validateTitle(self,title):
        if title=="":
            raise validatorMovieExceptions("The title cannot be empty!\n")
        
    def validateGenre(self,genre):
        if genre=="":
            raise validatorMovieExceptions("The genre cannot be empty!\n")
        
    def validateDescription(self,descr):
        if descr=="":
            raise validatorMovieExceptions("The description cannot be empty!\n")
    
    def validate(self,movie):
        self.validateId(movie.getId())
        self.validateTitle(movie.getTitle())
        self.validateGenre(movie.getGenre())
        self.validateDescription(movie.getDescription())
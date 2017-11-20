'''
Created on Nov 13, 2017

@author: Monica
'''
from domain.movie import movie

class moviesController:
    def __init__(self,repo,valid):
        '''
        initializes the movie
        in:    -> repo:repoMovies
               -> valid:validatorMovie
        '''
        self.__repository=repo
        self.__validator=valid
        
    def createMovie(self,idM,title,genre,description):
        '''
        creates a movie
        in:   ->idM:int unique
              ->title:string
              ->genre:string
              ->description:string
        out:the movie created
        '''
        m=movie(idM,title,genre,description)
        self.__validator.validate(m)
        self.__repository.store(m)
        return m
    
    def update(self,idM,title,genre,descr):
        '''
        updates a movie 
        '''
        m=movie(idM,title,genre,descr)
        self.__validator.validate(m)
        self.__repository.modify(m)
    
    def remove(self,idM):
        '''
        removes a movie with an unique id:idM(in ->integer number)
        '''
        self.__repository.remove(idM)
    
    def removeAll(self):
        '''
        removes all movies
        '''
        self.__repository.clearList()
        
    def find(self,nameK,valueK):
        '''
        find movies with a specified key
        in:  ->nameK(the name of key):can be id/title/genre
             ->valueK(the value of key)
        out: the movie
        '''
        return self.__repository.find(nameK,valueK)
    
    def filterBy(self,nameK,valueK):
        '''
        find movies with a specified key whose value is a string
        in:  ->nameK(the name of key):can be title/genre in this case
             ->valueK(the value of key)
        out: the movie
        '''
        allMovies=self.__repository.getAll()
        filteredMovies=[]
        for i in range(len(allMovies)):
            if (nameK=="title" and allMovies[i].getTitle()==valueK) or\
                (nameK=="genre" and allMovies[i].getGenre()==valueK) :
                filteredMovies.append(allMovies[i])
        return filteredMovies
       
    
    def sortBy(self,nameK):
        '''
        sorts the list of movies by a specified key,whose value is an integer number
        in:nameK (the key)
        out:-
        '''
        if nameK=="id":
            return sorted(self.__repository.getAll(), key=lambda k:k.getId(),reverse=True)
        
    def get(self,idM):
        '''
        gets a movie
        in:the unique id (idM) -an integer number
        out:the movie
        '''
        return self.__repository.get(idM)
    
    def getAll(self):
        '''
        gets all the movies
        in:-
        out:the list of movies
        '''
        return self.__repository.getAll()
    
    def getNrMovies(self):
        '''
        gets the number of movies
        in:-
        out:the number of movies
        '''
        return self.__repository.sizeOfList()
    



    
'''
Created on Nov 13, 2017

@author: Monica
'''
class moviesRepositoryExceptions(Exception):
        pass
        
class moviesRepository:
    '''
    stores movies in memory
    '''
    def __init__(self):
        self.__movies={}
        
    def store(self,movie):
        '''
        stores a movie in memory if it does not exist yet,else raise an exception
        in:movie
        out:-
        '''
        if movie.getId() in self.__movies:
            raise moviesRepositoryExceptions("This movie already exists! Give another id!")
        else:
            self.__movies[movie.getId()]=movie
            
    def clearList(self):
        '''
        remove all the movies
        '''
        if self.sizeOfList()!=0:
            self.__movies={}
        else:
            raise moviesRepositoryExceptions("The list has no movies!\n")
    def modify(self,movie):
        '''
        modifies a movie that already exists,else raise an exception
        in:movie
        out:-
        '''        
        for i in self.__movies.values():
            if i.getId()==movie.getId():
                self.__movies[movie.getId()]=movie
            else:
                raise moviesRepositoryExceptions("This id does not exist in the movies list!")
    
    def sizeOfList(self):
        '''
        the numbers of movies
        in:-
        out:the numbers of movies (an integer number)
        '''
        return len(self.__movies)
    
    def remove(self,idM):
        '''
        removes a movie that exists,else raise an exception
        in:movie
        out:
        
        '''
        try:
            self.__movies.pop(idM)
        except KeyError:
            raise moviesRepositoryExceptions("This movie does not exist in the movies list!")
    
    def find(self,nameK,valueK,index=0):
        '''
        finds all movies after a key
        in: ->nameK(the name of key):can be id/title/genre
            ->valueK(the value of the key): the value of id/title/genre
            ->index: starts from 0 until the end of the movies list
        out: list of movies
        '''
        allMovies=list(self.__movies.values())
        foundMovies=[]
        for index in range(len(allMovies)):
            if (nameK=='id' and allMovies[index].getId()==valueK) or\
               (nameK=='title' and allMovies[index].getTitle()==valueK) or\
               (nameK=='genre' and allMovies[index].getGenre()==valueK):
                foundMovies.append(allMovies[index])
                
        return foundMovies

    def get(self,idM):
        '''
        gets the movie 
        in: ->the unique id (an integer number)
        out:the movie or the exception when the id does not exist in the list
        '''
        try:
            return self.__movies[idM]
        except KeyError:
            raise moviesRepositoryExceptions("The id does not exist!\n")
        
    def getAll(self):
        '''
        gets all the movies 
        in:-
        out: the list of movies
         '''
        return list(self.__movies.values())
            
        

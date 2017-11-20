'''
Created on Nov 13, 2017

@author: Monica
'''
from repository.repoMovies import moviesRepositoryExceptions
from validator.validatorMovie import validatorMovieExceptions
from validator.validatorCommands import validatorCommands,\
    validatorCommandsException
class moviesMenu:
    def __init__(self,contrlMovie):
        self.__controllerMovie=contrlMovie
        self.valid=validatorCommands()
    def addMovie(self):
        '''
        adds a movie to a customer
        '''
        idM=input("Give the id:")
        title=input("Give the title:")
        genre=input("Give the genre:")
        description=input("Give the description:")
        try:
            m=self.__controllerMovie.createMovie(idM,title,genre,description)
            print(" Movie " + m.getTitle() + " added succesfully!\n")
        except moviesRepositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
            
    def removeAMovie(self):
        '''
        removes a movie from a customer
        '''
        idM=input("Give the id:")
        try:
            self.__controllerMovie.remove(idM)
            print("Movie removed succesfully!\n")
        except moviesRepositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def removeAllMovies(self):
        '''removes all movies from a customer'''
        try:
            self.__controllerMovie.removeAll()
            print("Movies removed succesfully!\n")
        except moviesRepositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def findById(self):
        '''finds a movie by id'''
        idM=input("Give the id:")
        try:
            m=self.__controllerMovie.find("id",idM)
            if len(m)==0:
                print("No movie found!\n")
            else:
                print("Movie found succesfully ! "+m.__str__())
        except moviesRepositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def findByTitle(self):
        '''finds movies by title'''
        title=input("Give the title:")
        try:
            m=self.__controllerMovie.find("title",title)
            if len(m)==0:
                print("No movie found!\n")
            else:
                i=0
                while i<len(m):
                    print("Movie found succesfully! "+m[i].__str__())
                    i+=1
        except moviesRepositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def findByGenre(self):
        '''finds movies by genre'''
        g=input("Give the genre:")
        try:
            m=self.__controllerMovie.find("genre",g)
            if len(m)==0:
                print("No movie found!\n")
            else:
                i=0
                while i<len(m):
                    print("Movie found succesfully! "+m[i].__str__())
                    i+=1
        except moviesRepositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def sortById(self):
        '''sorts the movies by id'''
        if self.__controllerMovie.getNrMovies()==0:
            print("The list has no movies!\n")
        else:
            movies=self.__controllerMovie.sortBy("id")
            for i in movies:
                print(i.__str__())
            print("List sorted succesfully!\n")
        
    def filterByTitle(self):
        '''
        prints the movies with a specified title
        '''
        title=input("Give the title:")
        try:
            m=self.__controllerMovie.filterBy("title",title)
            if len(m)==0:
                print("No movie found with specified title!\n")
            else:
                i=0
                while i<len(m):
                    print("Movie with the title "+title+":"+m[i].__str__())
                    i+=1
        except moviesRepositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def filterByGenre(self):
        '''
        prints the movies with a specified genre
        '''
        genre=input("Give the genre:")
        try:
            m=self.__controllerMovie.filterBy("genre",genre)
            if len(m)==0:
                print("No movie found with specified genre!\n")
            else:
                i=0
                while i<len(m):
                    print("Movie with the genre "+genre+":"+m[i].__str__())
                    i+=1
        except moviesRepositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
    
            
    def updateMovie(self):
        '''modifies a movie from a customer'''
        #try:
        newId=input("Give the id:")
        newTitle=input("Give a new title:")
        newGenre=input("Give a new genre:")
        newDescription=input("Give a new description:")
        try:
            self.__controllerMovie.update(newId,newTitle,newGenre,newDescription)
            print("Movie modified succesfully!")
        except moviesRepositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def showAMovie(self):
        '''shows a movie with an given id'''
        try:
            self.findById()
        except moviesRepositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def showAllMovies(self):
        '''shows all the movies'''
        printed=False
        for i in self.__controllerMovie.getAll():
            print(i.__str__())
            printed=True
        if printed==False:
            print("There are't movies yet!\n")
            
    def show(self):
        while True:
            print("===Movies menu===")
            print("1.Add")
            print("2.Remove")
            print("3.Find")
            print("4.Update")
            print("5.Show")
            print("6.Sort by id")
            print("7.Filter")
            print("0.Exit")
            print()
            cmd=input("Give command:")
            try:
                self.valid.validate(cmd,7)
                com=int(cmd)
                if com==0:
                    return
                elif com==1:
                    self.addMovie()
                elif com==2:
                    print("--Remove menu--")
                    print("1.Remove a movie")
                    print("2.Remove all movies")
                    print("0.Exit")
                    print()
                    cmd=input("Give command:")
                    try:
                        self.valid.validate(cmd,2)
                        com=int(cmd)
                        if com==1:
                            self.removeAMovie()
                        elif com==2:
                            self.removeAllMovies()
                        elif com==0:
                            break
                    except validatorCommandsException as ex:
                        print(ex)
                elif com==3:
                    print("--Find menu--")
                    print("1.By id")
                    print("2.By title")
                    print("3.By genre")
                    print("0.Exit")
                    print()
                    cmd=input("Give command")
                    try:
                        self.valid.validate(cmd,2)
                        com=int(cmd)
                        if com==0:
                            break
                        elif com==1:
                            self.findById()
                        elif com==2:
                            self.findByTitle()
                        elif com==3:
                            self.findByGenre()
                    except validatorCommandsException as ex:
                        print(ex)
                elif com==4:
                    self.updateMovie()
                elif com==5:
                    print("--Show menu--")
                    print("1.Show a movie")
                    print("2.Show all movies")
                    print("0.Exit")
                    print()
                    cmd=input("Give command:")
                    try:
                        self.valid.validate(cmd,2)
                        com=int(cmd)
                        if com==0:
                            break
                        elif com==1:
                            self.showAMovie()
                        elif com==2:
                            self.showAllMovies()
                    except validatorCommandsException as ex:
                        print(ex)
                elif com==6:
                    self.sortById()
                elif com==7:
                    print("--Filter menu--")
                    print("1.Filter by title")
                    print("2.Filter by genre")
                    print("0.Exit")
                    cmd=input("Give command:")
                    try:
                        self.valid.validate(cmd,2)
                        com=int(cmd)
                        if com==0:
                            break
                        elif com==1:
                            self.filterByTitle()
                        elif com==2:
                            self.filterByGenre()
                    except validatorCommandsException as ex:
                        print(ex)
                
            except validatorCommandsException as ex:
                print(ex)

'''
Created on Nov 13, 2017

@author: Monica
'''
from repository.repository import repositoryExceptions
from validator.validatorMovie import validatorMovieExceptions
from validator.validatorCommands import validatorCommands,\
    validatorCommandsException
class moviesMenu:
    def __init__(self,srvMovie,srvRent):
        '''
        initialize the class
        in:    ->srvMovie=the movie service
        '''
        self.__serviceMovie=srvMovie
        self.valid=validatorCommands()
        self.__serviceRent=srvRent
        
    def addMovie(self):
        '''
        adds a movie
        '''
        idM=input("Give the id:")
        title=input("Give the title:")
        genre=input("Give the genre:")
        description=input("Give the description:")
        try:
            idM=int(idM)
            m=self.__serviceMovie.createMovie(idM,title,genre,description)
            print(" Movie " + m.getTitle() + " added succesfully!\n")
        except ValueError:
            print("The id can 't be string or empty!\n")
        except repositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
            
    def removeAMovie(self):
        '''
        removes a movie 
        '''
        idM=input("Give the id:")
        try:
            idM=int(idM)
            self.__serviceMovie.remove(idM)
            self.__serviceRent.removeAfterKey("movie",idM)
            print("Movie removed succesfully!\n")
        except ValueError:
            print("The id must be integer!\n")
        except repositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def removeAllMovies(self):
        '''removes all movies '''
        try:
            self.__serviceMovie.removeAll()
            self.__serviceRent.removeAll()
            print("Movies removed succesfully!\n")
        except repositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def findById(self):
        '''finds a movie by id'''
        idM=input("Give the id:")
        try:
            idM=int(idM)
            m=self.__serviceMovie.find("id",idM)
            if len(m)==0:
                print("No movie found!\n")
            else:
                print("Movie found succesfully ! "+m[0].__str__())
        except ValueError:
            print("Id invalid!\n")
        except repositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def findByTitle(self):
        '''finds movies by title'''
        title=input("Give the title:")
        try:
            m=self.__serviceMovie.find("title",title)
            if len(m)==0:
                print("No movie found!\n")
            else:
                i=0
                while i<len(m):
                    print("Movie found succesfully! "+m[i].__str__())
                    i+=1
        except repositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def findByGenre(self):
        '''finds movies by genre'''
        g=input("Give the genre:")
        try:
            m=self.__serviceMovie.find("genre",g)
            if len(m)==0:
                print("No movie found!\n")
            else:
                i=0
                while i<len(m):
                    print("Movie found succesfully! "+m[i].__str__())
                    i+=1
        except repositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def sortById(self):
        '''sorts the movies by id'''
        if self.__serviceMovie.getNrMovies()==0:
            print("The list has no movies!\n")
        else:
            movies=self.__serviceMovie.sortBy("id")
            for i in movies:
                print(i.__str__())
            print("List sorted succesfully!\n")
        
    def filterByTitle(self):
        '''
        prints the movies with a specified title
        '''
        title=input("Give the title:")
        try:
            m=self.__serviceMovie.filterBy("title",title)
            if len(m)==0:
                print("No movie found with specified title!\n")
            else:
                i=0
                while i<len(m):
                    print("Movie with the title "+title+":"+m[i].__str__())
                    i+=1
        except repositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
        
    def filterByTitleRec(self):
        '''
        prints the movies with a specified title
        '''
        title=input("Give the title:")
        try:
            found=[]
            m=self.__serviceMovie.filterByRec("title",title,self.__serviceMovie.getAll(),found)
            
            if len(m)==0:
                print("No movie found with specified title!\n")
            else:
                i=0
                while i<len(m):
                    print("Movie with the title "+title+":"+m[i].__str__())
                    i+=1
        except repositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def filterByGenre(self):
        '''
        prints the movies with a specified genre
        '''
        genre=input("Give the genre:")
        try:
            m=self.__serviceMovie.filterBy("genre",genre)
            if len(m)==0:
                print("No movie found with specified genre!\n")
            else:
                i=0
                while i<len(m):
                    print("Movie with the genre "+genre+":"+m[i].__str__())
                    i+=1
        except repositoryExceptions as ex:
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
            newId=int(newId)
            self.__serviceMovie.update(newId,newTitle,newGenre,newDescription)
            print("Movie modified succesfully!")
        except ValueError:
            print("Invalid id!\n")
        except repositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def showAMovie(self):
        '''shows a movie with an given id'''
        try:
            self.findById()
        except repositoryExceptions as ex:
            print(ex)
        except validatorMovieExceptions as ex:
            print(ex)
            
    def showAllMovies(self):
        '''shows all the movies'''
        printed=False
        for i in self.__serviceMovie.getAll():
            print(i.__str__())
            printed=True
        if printed==False:
            print("There are't movies yet!\n")
            
    def populateRandom(self,limit):
        '''populate the repository with random elements
        '''
        while limit!=0:
            try:
                limit=self.__serviceMovie.populateRandom(limit) 
                print("The repository was populated successfully!\n")
            except repositoryExceptions :
                print("The repository was populated successfully but with less movies!\n")
                break
    def groupeByGenre(self):
        '''
        prints the id sum of movies with the same genre
        '''
        movies=self.__serviceMovie.getAll()
        grouped=[]
        for i in movies:
            grouped=[]
            gen=i.getGenre()
            for j in movies:
                if j.getGenre()==gen:
                    grouped.append(i)
                    movies.remove(j)
            summ=0
            for j in range(len(grouped)):
                summ+=grouped[j].getId()
            print("The sum id with the genre " +gen+" is: "+str(summ)+".")
            
    def show(self):
        while True:
            print("\n===Movies menu===")
            print("1.Add")
            print("2.Remove")
            print("3.Find")
            print("4.Update")
            print("5.Show")
            print("6.Sort by id")
            print("7.Filter")
            print("8.Populate random")
            print("9.The id sum of all genre")
            print("0.Exit")
            print()
            cmd=input("Give command:")
            try:
                self.valid.validate(cmd,9)
                com=int(cmd)
                if com==0:
                    return
                elif com==1:
                    self.addMovie()
                elif com==2:
                    print("\n--Remove menu--")
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
                    print("\n--Find menu--")
                    print("1.By id")
                    print("2.By title")
                    print("3.By genre")
                    print("0.Exit")
                    print()
                    cmd=input("Give command:")
                    try:
                        self.valid.validate(cmd,3)
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
                    print("\n--Show menu--")
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
                    print("\n--Filter menu--")
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
                elif com==8:
                    try:
                        limit=int(input("Give the number of movies:"))
                        self.populateRandom(limit)
                    except ValueError:
                        print("The limit must be an integer number!\n")
                    
                elif com==9:
                    self.groupeByGenre()
            except validatorCommandsException as ex:
                print(ex)


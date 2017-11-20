'''
Created on Nov 15, 2017

@author: Monica
'''
from domain.movie import movie
from controller.controllerM import moviesController
from validator.validatorMovie import validatorMovie
from repository.repoMovies import moviesRepository
def testMovie():
    m=movie(1,"Me before you","Love","A good movie")
    assert m.getId()==1
    assert m.getTitle()=="Me before you"
    assert m.getGenre()=="Love"
    assert m.getDescription()=="A good movie"
    m.setId(2)
    assert m.getId()==2
    m.setTitle("It")
    assert m.getTitle()=="It"
    m.setGenre("Horror")
    assert m.getGenre()=="Horror"
    m.setDescription("Not so good")
    assert m.getDescription()=="Not so good"
    
    m2=movie(2,"It","Horror","Not so good")
    assert m==m2
    
    
def testControllerM():
    c=moviesController(moviesRepository(),validatorMovie())
    m=c.createMovie(1,"The same","Tragedy","English movie")
    assert m.getId()==1
    assert m.getTitle()=="The same"
    assert m.getGenre()=="Tragedy"
    assert m.getDescription()=="English movie"

    c.update(1,"Divergent","Action","One of the best")
    new=movie(1,"Divergent","Action","One of the best")
    assert c.get(1)==new
    
    c.remove(1)
    assert c.getNrMovies()==0

    m=c.createMovie(1,"Inception","Action","Awesome")
    c.find("id",1)
    assert c.get(1)==m

    assert c.getNrMovies()==1
    
def testRepositoryM():
    repo=moviesRepository()
    mov=movie(1,"Divergent","Action","Wonderful")
    repo.store(mov)
    assert repo.get(1)==mov
    new=movie(1,"The pretty woman","Love","Good")
    repo.modify(new)
    assert repo.get(1)==new
    assert repo.sizeOfList()==1
    assert repo.find("id",1)==[new]
    assert repo.find("title","The pretty woman")==[new]
    assert repo.find("genre","Love")==[new]
    repo.clearList()
    assert repo.sizeOfList()==0
    mov=movie(1,"Divergent","Action","Wonderful")
    repo.store(mov)
    repo.remove(1)
    assert repo.sizeOfList()==0
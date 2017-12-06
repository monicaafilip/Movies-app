'''
Created on Nov 23, 2017

@author: Monica
'''
from domain.rent import rent
from repository.repository import repository
from validator.validatorRent import validatorRent
from service.serviceR import rentsService

def testRent():
    r=rent(1,2,3)
    assert r.getId()==1
    assert r.getMovie()==2
    assert r.getCustomer()==3
    
    r.setMovie(10)
    r.setCustomer(10)
    assert r.getMovie()==10
    assert r.getCustomer()==10
    
    another=rent(1,10,10)
    assert r==another
    
def testRepositoryR():
    repo=repository()
    r=rent(1,2,3)
    repo.store(r)
    assert repo.get(1)==r
    assert repo.sizeOfList()==1
    assert repo.find("id",1)==[r]
    assert repo.find("idC",3)==[r]
    assert repo.find("idM",2)==[r]
    repo.clearList()
    assert repo.sizeOfList()==0
    r=rent(1,7,9)
    repo.store(r)
    repo.remove(1)
    assert repo.sizeOfList()==0
    
def testServiceR():
    rentRepository=repository()
    ctrl=rentsService(rentRepository,validatorRent())
    r=ctrl.createRent(1,4,7)
    assert r.getId()==1
    assert r.getMovie()==4
    assert r.getCustomer()==7
    
    ctrl.remove(1)
    assert ctrl.getNrCustomers()==0

    r=ctrl.createRent(1,10,12)
    ctrl.find("id",1)
    assert ctrl.get(1)==r

    assert ctrl.getRents()==1
    r1=rent(1,2,3)
    rentRepository.store(r1)
    r2=rent(2,2,4)
    rentRepository.store(r2)
    r3=rent(3,5,7)
    rentRepository.store(r3)
    assert ctrl.getMostRentedMovies==[[1,2,3],[2,2,4]]
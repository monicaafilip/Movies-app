'''
Created on Nov 15, 2017

@author: Monica
'''
from domain.customer import customer
from controller.controllerC import customersController
from repository.repoCustomers import customersRepository
from validator.validatorCustomer import validatorCustomer
def testCustomer():
    c=customer(1,"Popescu",1234567898765)
    assert c.getId()==1
    assert c.getName()=="Popescu"
    assert c.getCnp()==1234567898765
    c.setId(2)
    assert c.getId()==2
    c.setName("Ionescu")
    assert c.getName()=="Ionescu"
    c.setCnp(1230507098765)
    assert c.getCnp()==1230507098765
  
    c1=customer(2,"Ionescu",1230507098765)
    assert c==c1
    
def testControllerC():
    ctrl=customersController(customersRepository(),validatorCustomer())
    c=ctrl.createCustomer(1,"Berinde",1672030123345)
    assert c.getId()==1
    assert c.getName()=="Berinde"
    assert c.getCnp()==1672030123345

    ctrl.update(1,"Modoi",1672030128888)
    new=customer(1,"Modoi",1672030128888)
    assert ctrl.get(1)==new
    
    ctrl.remove(1)
    assert ctrl.getNrCustomers()==0

    c=ctrl.createCustomer(1,"Istvanc",1672030129999)
    ctrl.find("id",1)
    assert ctrl.get(1)==c

    assert ctrl.getNrCustomers()==1
    
def testRepositoryC():
    repo=customersRepository()
    cust=customer(1,"Andrada",2802020112345)
    repo.store(cust)
    assert repo.get(1)==cust
    new=customer(1,"Diana",2820101334543)
    repo.modify(new)
    assert repo.get(1)==new
    assert repo.sizeOfList()==1
    assert repo.find("id",1)==[new]
    assert repo.find("name","Diana")==[new]
    assert repo.find("cnp",2820101334543)==[new]
    repo.clearList()
    assert repo.sizeOfList()==0
    cust=customer(1,"Diana",2820101334543)
    repo.store(cust)
    repo.remove(1)
    assert repo.sizeOfList()==0
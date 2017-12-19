'''
Created on Dec 19, 2017

@author: Monica
'''
class generic_sort:
    def __init__(self,lst,key,reverse):
        self.__lst = lst
        self.__key = key
        self.__reverse = reverse

    def get_lst(self):
        return self.__lst


    def get_key(self):
        return self.__key


    def get_reverse(self):
        return self.__reverse

    def sort(self):
        pass
    
    def _in_order(self,e1,e2,eq=True):
        '''
        verify what is the order to know how to sort,reverse or not
        what is the key
        in:
            e1,e2:two elements which must be sorted
            eq:a variable which will be returned if the elements are equal
        '''
        if self.__key==None:
            self.__key=lambda x:x
        elif self.__key(e1)==self.__key(e2):
            return eq
        if not self.__reverse:
            return self.__key(e1)<self.__key(e2)
        return self.__key(e1)>self.__key(e2)

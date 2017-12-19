'''
Created on Dec 18, 2017

@author: Monica
'''
from sort.generic_sort import generic_sort
class bingoSort(generic_sort):
    def __init__(self,lst,key,reverse):
        super().__init__(lst, key, reverse)
        
        
    def sort(self,lst):
        i=1
        while i<len(lst):
            aux=lst[i]
            poz=i
            
            while poz>0 and not self._in_order(lst[poz-1],aux):
                lst[poz]=lst[poz-1]
                poz-=1
                
            lst[poz]=aux
            j=i+1
            keep=0
            while j<len(lst):
                k=j
                if lst[j]==aux:
                    keep+=1
                    k=j
                    poz+=1
                    while j>poz and not self._in_order(lst[j-1],aux) :
                        lst[j]=lst[j-1]
                        j-=1
                    lst[j]=aux
                j=k+1    
            
            if keep!=0:
                i+=keep
            else:
                i+=1
                
        return lst
        
        
'''
def bingoSort(lst):
    i=1
    while i<len(lst):
        aux=lst[i]
        poz=i
        
        while poz>0 and lst[poz-1]>aux:
            lst[poz]=lst[poz-1]
            poz-=1
            
        lst[poz]=aux
        j=i+1
        keep=0
        while j<len(lst):
            k=j
            if lst[j]==aux:
                keep+=1
                k=j
                poz+=1
                while j>poz and lst[j-1]>aux :
                    lst[j]=lst[j-1]
                    j-=1
                lst[j]=aux
            j=k+1    
        
        if keep!=0:
            i+=keep
        else:
            i+=1
            
    return lst
'''

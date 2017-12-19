'''
Created on Dec 19, 2017

@author: Monica
'''
from sort.algorithms.Algorithm import Algorithm
class sorting(object):
    @staticmethod
    def sort(lst,*,key=None,reverse=False,algorithm=Algorithm.BINGO_SORT):
        sortingAlg=algorithm.value(lst,key,reverse)
        return sortingAlg.sort(lst)
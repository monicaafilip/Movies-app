'''
Created on Dec 19, 2017

@author: Monica
'''
from enum import unique,Enum
from sort.algorithms.mergeSort import mergeSort
from sort.algorithms.bingoSort import bingoSort

@unique
class Algorithm(Enum):
    MERGE_SORT=mergeSort
    BINGO_SORT=bingoSort
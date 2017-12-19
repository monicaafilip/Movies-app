'''
Created on Dec 18, 2017

@author: Monica
'''
from sort.generic_sort import generic_sort
class mergeSort(generic_sort):
    def __init__(self,lst,key,reverse):
        super().__init__(lst, key, reverse)
        
    def sort(self, seq):
        '''
    Sorts a sequence of integers.

    @param seq: an unsorted tuple or list.
    @return:    a new tuple with elements in @seq sorted in ascending order. 
        '''
        if(len(seq) <= 1):
            return seq
        else:
            return self._merge(self.sort(seq[0:int((len(seq) / 2))]),\
                               self.sort(seq[int((len(seq) / 2)):]))

    def _merge(self, leftSortedSeq, rightSortedSeq):
        if(len(leftSortedSeq) == 0):
            return rightSortedSeq
        elif(len(rightSortedSeq) == 0):
            return leftSortedSeq
    
        leftPointer = 0
        rightPointer = 0
        mergedSeq = []
        mergedSeqLength = len(leftSortedSeq) + len(rightSortedSeq)
        for i in range(mergedSeqLength):
    
            try:
                smallestInLeft = leftSortedSeq[leftPointer]
            except IndexError:
                mergedSeq += rightSortedSeq[rightPointer:]
                return list(mergedSeq)
    
            try:
                smallestInRight = rightSortedSeq[rightPointer]
            except IndexError:
                mergedSeq += leftSortedSeq[leftPointer:]
                return list(mergedSeq)
            if self._in_order(smallestInLeft, smallestInRight):
                    mergedSeq.append(leftSortedSeq[leftPointer])
                    leftPointer += 1
            else:
                mergedSeq.append(rightSortedSeq[rightPointer])
                rightPointer += 1
        
        return list(mergedSeq)



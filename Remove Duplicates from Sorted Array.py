# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 23:04:46 2017

@author: James
"""
"""
        :type nums: List[int]
        :rtype: int
        nums is a sorted array
        """  
def removeDuplicates(self, nums):  
    temp = nums[:]
    
    if len(nums)<2:
       return len(nums)
    else:
        for i in temp:
           count=1
           for j in nums:
              if i == j:
                  if count>1:
                      nums.remove(i)
                  else:
                  
                      count=count+1
                    
    return len(nums)
    """
    class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        if not A:
            return 0

        newTail = 0

        for i in range(1, len(A)):
            if A[i] != A[newTail]:
                newTail += 1
                A[newTail] = A[i]

        return newTail + 1
     """
     """
     since this list is sorted
     only check whether its neoghbor is the same
     1. if not the same, newtail proceed first by +1 to the initial i
     position, then i proceed by i+1
     2. once is the same as next one, new tail stops, and i keeps going
     till meet a different one
     then by newtail proceed first by +1 
     and switch the different one to the neighbour
     
    

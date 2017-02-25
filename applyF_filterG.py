# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 00:09:32 2017

@author: James
"""

def applyF_filterG(L, f, g):
    """
    Assumes L is a list of integers
    Assume functions f and g are defined for you. 
    f takes in an integer, applies a function, returns another integer 
    g takes in an integer, applies a Boolean function, 
        returns either True or False
    Mutates L such that, for each element i originally in L, L contains  
        i if g(f(i)) returns True, and no other elements
    Returns the largest element in the mutated L or -1 if the list is empty
    """
    
    copied_L=L[:]
    for j in copied_L:
            
       if not g(f(j)):
         L.remove(j)
                         
    if len(L)==0:
       return -1
    else:
       return max(L)
           
            
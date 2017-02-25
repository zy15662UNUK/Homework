# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:10:11 2017

@author: James
"""

def deep_reverse(L):
    """ assumes L is a list of lists whose elements are ints
    Mutates L such that it reverses its elements and also 
    reverses the order of the int elements in every element of L. 
    It does not return anything.
    """
    for element in L:
        element.reverse()
    L.reverse()
    
    
   
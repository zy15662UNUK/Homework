# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 22:06:20 2017

@author: James
"""

def dotProduct(listA, listB):
    '''
    listA: a list of numbers
    listB: a list of numbers of the same length as listA
    '''
    dotsum=0
    for i in range(len(listA)):
        dotsum=dotsum+listA[i]*listB[i]
    return dotsum

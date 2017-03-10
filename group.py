# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 22:24:02 2017

@author: James
"""

def group(arr):
    """
    Sam is an avid collector of numbers. Every time he finds a new number he throws it on the top of his number-pile. Help Sam organise his collection so he can take it to the International Number Collectors Conference in Cologne.

Given an array of numbers, your function should return an array of arrays, where each subarray contains all the duplicates of a particular number. Subarrays should be in the same order as the first occurence of the number they contain:

group([3, 2, 6, 2, 1, 3])
>>> [[3, 3], [2, 2], [6], [1]]
Assume the input is always going to be an array of numbers. If the input is an empty array, an empty array should be returned.
    """
    if arr == []:
        return []
    out=[]
    repeat=[]
    for i in arr:
        if arr.count(i)==1:
            out.append([i])
        elif i not in repeat:
            repeat.append(i)
            insert=[]
            for j in range(arr.count(i)):
                insert.append(i)
            out.append(insert)
    return out
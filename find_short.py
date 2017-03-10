# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 23:00:04 2017

@author: James
"""

def find_short(s):
    """
    x Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
    """
    
    li=s.split(' ')
    shortest=len(li[0])
    for i in li:
        if len(i)<=shortest:
            shortest=len(i)
    return shortest
    
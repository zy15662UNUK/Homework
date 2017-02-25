# -*- coding: utf-8 -*-
"""
Created on Tue Feb 14 17:13:05 2017

@author: James
"""
def help_flatten(copy_of_aList,aList):
    for i in aList:
        if type(i) != list:
            copy_of_aList.append(i)
        else:
            help_flatten(copy_of_aList,i)
    return copy_of_aList
def flatten(aList):
    ''' 
    aList: a list 
    Returns a copy of aList, which is a flattened version of aList 
    '''
    copy_of_aList=[]
    
    help_flatten(copy_of_aList,aList)
            
    return copy_of_aList
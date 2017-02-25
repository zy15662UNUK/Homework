# -*- coding: utf-8 -*-
"""
Created on Tue Feb  7 22:39:28 2017

@author: James
"""

def twoSum(a,num,target):
    for i in range(len(num)):
        for j in range(i+1,len(num)):
            if num[i]+num[j]==target:
              
              return [i,j]

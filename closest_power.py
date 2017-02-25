# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 21:07:38 2017

@author: James
"""

def closest_power(base, num):
    '''
    base: base of the exponential, integer > 1
    num: number you want to be closest to, integer > 0
    Find the integer exponent such that base**exponent is closest to num.
    Note that the base**exponent may be either greater or smaller than num.
    In case of a tie, return the smaller value.
    Returns the exponent.
    '''
   
    if num ==1:
      return 0
    elif base == num:
        return 1
    elif base > num:
        diff = abs(base**0-num)
        a=base-num
        if a < diff:
            return 1
        else:
            return 0
    else:
        n=1
        diff=[]
        while base**n <= num:
            b=num-base**n
            diff.append(b)
            n=n+1
            print(diff)
        print('n: ',n)   
        if min(diff)>(base**n-num):
            print('min diff: ',min(diff))
            return n
        else:
            print('index',diff.index(min(diff)))
            return 1+diff.index(min(diff))
            
    
        
            
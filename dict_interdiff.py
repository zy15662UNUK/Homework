# -*- coding: utf-8 -*-
"""
Created on Mon Feb 13 20:09:14 2017

@author: James
"""

def dict_interdiff(d1, d2):
    '''
    d1, d2: dicts whose keys and values are integers
    Returns a tuple of dictionaries according to the instructions above
    '''
    same={}
    diff={}
    out=()
    if len(d1) >= len(d2):
      long=d1
      short=d2
    else:
         short=d1
         long=d2
    sort_long=sorted(long.keys())
    sort_long_clone=sort_long[:]
    sort_short=sorted(short.keys())
    sort_short_clone=sort_short[:]
    print('sort long ',sort_long)
    print('sort short ', sort_short)
    
    for i in sort_long_clone:
        if i in sort_short_clone:
            same[i]=f(d1[i],d2[i])
            sort_long.remove(i)
            sort_short.remove(i)
            print('sort long ',sort_long)
            print('sort short ', sort_short)
    if len(sort_short)==0:
        for i in sort_long:
            diff[i]=long[i]
    else:
        for i in sort_short:
          for j in sort_long:
            if i>j:
                diff[j]=long[j]
          
                diff[i]=short[i]
            else:
                diff[i]=short[i]
                diff[j]=long[j]
    print('diff ',diff)
    out=out+(same,)
    out=out+(diff,)
    return out
            
    
    
    
            
            
        
     
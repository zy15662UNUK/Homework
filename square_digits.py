# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 21:55:59 2017

@author: James
"""

def square_digits(num):
    """
    Welcome. In this kata, you are asked to square every digit of a number.

For example, if we run 9119 through the function, 811181 will come out.

Note: The function accepts an integer and returns an integer
    """
    num=str(num)
    out=''
    for i in num:
        digit=int(i)
        out=out+str(digit**2)
    return int(out)
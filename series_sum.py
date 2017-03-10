# -*- coding: utf-8 -*-
"""
Created on Thu Mar  2 20:10:38 2017

@author: James
"""

def series_sum(n):
    '''
    Your task is to write a function which returns the sum of following series upto nth term(parameter).

Series: 1 + 1/4 + 1/7 + 1/10 + 1/13 + 1/16 +...
Rules:

You need to round the answer upto 2 decimal places and return it as String.
If the given value is 0 then it should return 0.00
You will only be given Natural Numbers as arguments.
Examples:

SeriesSum(1) => 1 = "1"
SeriesSum(2) => 1 + 1/4 = "1.25"
SeriesSum(5) => 1 + 1/4 + 1/7 + 1/10 + 1/13 = "1.57"
    '''
    from decimal import getcontext, Decimal
    deno=1
    numer=1
    sum1=0
    if n ==0:
        return '0.00'
    if n==1:
        return '1.00'
    for i in range(n):
        sum1=sum1+numer/deno
        deno += 3
    getcontext().prec = 3
    return str(round(Decimal(sum1),2))
        
        
        
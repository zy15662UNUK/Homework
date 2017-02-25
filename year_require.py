# -*- coding: utf-8 -*-
"""
Created on Wed Feb  1 15:25:00 2017

@author: James
"""

def min(balance ,annualInterestRate, n):
    
    for i in range(1:13):
        
         balance = balance - 10*n
         balance = balance + balance*annualInterestRate/12
    return i
    return balance
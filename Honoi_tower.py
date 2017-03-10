# -*- coding: utf-8 -*-
"""
Created on Mon Feb  6 22:13:44 2017

@author: James
"""
def printMove(fr,to):
    print('move from '+str(fr)+' to '+str(to))
    """
    first define a action function for your desire output
    
    """
def Towers(n,fr,to,spare):
    if n==1:
      printMove(fr,to)
      """
      the base case: while only one piece, directly move from start to end
      """
    else:
         Towers(n-1,fr,spare,to)
         """
         Recurrsion : consider all the smaller part as an integral, move it
         to the spare, then move the largest to the spare
         """
         Towers(1,fr,to,spare)
         """
         move the largest to the end
         """
         
         Towers(n-1,spare,to,fr)
         """
         move smaller from the spare to the end
         """

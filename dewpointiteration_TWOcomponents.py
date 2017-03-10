# -*- coding: utf-8 -*-
"""
Created on Sat Feb 11 14:27:00 2017

@author: James
"""

def sigma_x(x):
    sigma=0
    for i in range(1,3):
        sigma=sigma+x[i]
    return sigma
def input_k(k):
    for i in range(1,3):
        k[i]=input('enter the new k value of component '+str(i)+': ')
        k[i]=float(k[i])
    return k
def calculate_x(k,x,y1,y2):
    x[1]=y1/k[1]
    x[2]=y2/k[2]

    return x
        
   
def dewpointiteration_TWOcomponents(y1,y2,p,guessT):
    print('set pressure at '+str(p))
    print('use the guess T to get initial value of k')
    k1=input('read from temperature and pressure of component 1: ')
    k2=input('read from temperature and pressure of component 2: ')
    
    k1=float(k1)
    k2=float(k2)
    x=[0]
    k=[0]
    x.append(y1/k1)
    x.append(y2/k2)
    k.append(k1)
    k.append(k2)
    print('x: ',x)
    sigma=sigma_x(x)
    print('sigma: ',sigma)
    while abs(sigma-1)>0.01:
        knew=k[x.index(max(x))]*sigma
        print('the new k of component '+str(x.index(max(x)))+' is '+str(knew))
        input_k(k)
        print('k: ',k)
        calculate_x(k,x,y1,y2)
        print('x: ',x)
        sigma=sigma_x(x)
        print('sigma: ',sigma)
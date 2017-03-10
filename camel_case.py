# -*- coding: utf-8 -*-
"""
Created on Fri Mar  3 22:39:25 2017

@author: James
"""

def camel_case(string):
    """
    Write simple .camelcase method (camel_case function in PHP) for strings. All words must have their first letter capitalized without spaces.

For instance:

camelcase("hello case") => HelloCase
camelcase("camel case word") => CamelCaseWord
    """
    if string == '':
        return ''
    string_list=string.split(' ')
    out=''
    head=''
    for i in string_list:
        if i == '':
            string_list.remove(i)
            
    for i in string_list:
        head=i[0].upper()
        out=out+head
        for j in range(1,len(i)):
            out=out+i[j]
    return out
            
        
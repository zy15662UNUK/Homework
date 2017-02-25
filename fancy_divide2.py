# -*- coding: utf-8 -*-
"""
Created on Sun Feb 12 19:39:22 2017

@author: James
"""

def fancy_divide2(list_of_numbers, index):
    try:
        try:
            raise Exception("0")
        finally:
            denom = list_of_numbers[index]
            for i in range(len(list_of_numbers)):
                list_of_numbers[i] /= denom
    except Exception as ex:
        print(ex)
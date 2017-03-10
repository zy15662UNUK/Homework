# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 20:44:32 2017

@author: James
"""

def longest_repetition(chars):
    """
    For a given string s find the character c with longest consecutive repetition and return a tuple (c, l) (in Haskell Just (Char, Int), in C# Tuple<char?, int>, in Shell a String of comma-separated values c,l) where l is the length of the repetition. If there are two or more characters with the same l return the first.

    For empty string return ('', 0) (in Haskell Nothing, in C# Tuple<char, int>(null, 0), in Shell ,0).

    Happy coding! :)
    """
    if chars == '':
        return ('',0)
    rep_char=chars[0]
    rep=1
    for i in range(len(chars)-1):
        count=1
        for j in range(i+1,len(chars)):
            if chars[i]==chars[j]:
                count += 1
            else:
                break
        if count > rep:
            rep_char=chars[i]
            rep=count
    return (rep_char, rep)
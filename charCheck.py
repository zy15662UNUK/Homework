# -*- coding: utf-8 -*-
"""
Created on Sat Mar  4 21:14:21 2017

@author: James
"""
def charCheck(text, mx, spaces):
    """
Write Cara a function charCheck() with the arguments:

"text": a string containing Cara's answer for the question
"max": a number equal to the maximum number of characters allowed in the answer
"spaces": a boolean which is True if spaces are included in the character count and False if they are not
The function charCheck() should return an array: [True, "Answer"] , where "Answer" is equal to the original text, if Cara's answer is short enough.

If her answer "text" is too long, return an array: [False, "Answer"]. The second element should be the original "text" string truncated to the length of the limit.

When the "spaces" argument is False, you should remove the spaces from the "Answer".

For example:

charCheck("Cara Hertz", 10, True) should return [ True, "Cara Hertz" ]
charCheck("Cara Hertz", 9, False) should return [ True, "CaraHertz" ]
charCheck("Cara Hertz", 5, True) should return [ False, "Cara " ]
charCheck("Cara Hertz", 5, False) should return [ False, "CaraH" ]
    """
    if spaces == True:
        i=0
        out=''
        if mx >= len(text):
            return [True,text]
        
        while i<mx:
            out=out+text[i]
            i=i+1
        if len(out)==len(text):
            return [True,out]
        else:
            return [False, out]
            
    else:
        k=0
        out=''
        text_list=text.split(' ')
        newtext=''
        for i in text_list:
            newtext += i
        if mx >= len(newtext):
            return [True,newtext]
         
        while k< mx:
            out=out+newtext[k]
            k=k+1
        if len(out)==len(newtext):
            return [True,out]
        else:
            return [False, out]
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 18:24:42 2018

@author: ntf-42
"""

def first():
    print('First module i made.')
    
def sayhi(name,age):
    print("hi "+name+","+str(age))    
    
    
sayhi("Vaibhav",22)

def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation =translation + "G"
            else:                
                translation =translation + "g"
        else:
            translation =translation + letter
    return translation

print(translate("FOg"))            
            
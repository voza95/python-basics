# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:21:46 2018

@author: ntf-42
"""

fw = open("sample.txt","w")
fw.write('Testing file in python\n')
fw.write('Let see if it workes.\n')
fw.close()


fa = open("sample.txt","a")
fa.write("In a tumultuous time befor dday.\n")
fa.write("There once was a guy name BJ.")
fa.close()
#r w r+ a(append)
fr = open('sample.txt','r')
text = fr.read()
print(text)
fr.close()
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 19:10:05 2018

@author: ntf-42
"""

def calculateP(y , z):
     return int( y ) + int( z )
     
def calculateResult( x, p ) :
        return int( x ) * int( p )
    
try:
    x = int(input('x: '))
    y = int(input('y: '))
    z = int(input('z: '))
    p = calculateP ( y , z )
    result = calculateResult( x , p )
    print(result)
except:
    print("Enter number only")
    



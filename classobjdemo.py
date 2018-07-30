# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 19:48:06 2018

@author: ntf-42
"""

class Enemy:
    life = 3
    def attack(self):
        print('ouch')
        self.life -= 1
        
    def checkLife(self):
        if self.life <= 0:
            print("dead")
        else:
             print(str(self.life))
             
enmeny1 = Enemy()

enmeny1.attack()
enmeny1.checkLife()
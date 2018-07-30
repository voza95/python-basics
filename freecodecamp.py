# -*- coding: utf-8 -*-
"""
Created on Sat Jul 14 15:58:52 2018

@author: ntf-42
"""
from math import *
import random
from student import Student

character_name="BJ"

student1 = Student("Jim","dsd",3.1,False)

print(student1.name)

print("In a tumultuous time befor dday ")
print("There once was a guy name "+ character_name)
print("With a chochlate box hair and face like a bear")
print("and the jekit he picket up on ebay")

test_str="This is a Demo String"

print(test_str.upper())

print(pow(5,9))


print(test_str[0:2].upper())
#if passed parameter is not persent in string programme will give error
print(test_str.index("i"))

#print(test_str.upper().isupper())
print(floor(8.99))
print(sqrt(81))
#print(type(character_name))

#Python by default takes only sting input
#name = str(input("Enter your name: "))
#print("Hello "+name)

print(random.randint(0,10))
try:
    # the space is called indent
    value = 10 / 0
    number = int(input("Enter a number: "))
    print(number)
except ZeroDivisionError as err:
    print(err)    
except ValueError:    
    print("Invaild input")
#my_list2 = my_list.copy()

#print(my_list2)
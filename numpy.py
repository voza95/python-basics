# -*- coding: utf-8 -*-
"""
Created on Fri Jul 20 17:52:46 2018

@author: ntf-42
"""

import numpy as np
import matplotlib.pyplot as plt


x = np.arange(0,3*np.pi,0.1)

y = np.sin(x)

plt.plot(x,y)

plt.show()

'''
a = np.array([(1,2,3),(4,5,6)])

print(a.sum()/6)

print(np.sqrt(a))
print(np.std(a))
print(a.sum(axis=1))
#Make 2D array
#a = np.array([(1,2,3,),(4,5,6)])
#print(a)
'''
#Space taken by numpy vs lsi
'''
S = range(1000)
print(sys.getsizeof(5)*len(S))
#24000
D = np.arange(1000)
print(D.size*D.itemsize)
#8000
'''

#Speed numpy vs. list
'''
SIZE = 10000

L1 = range(SIZE)
L2 = range(SIZE)

A1 = np.arange(SIZE)
A2 = np.arange(SIZE)

start =time.time()
result = [(x,y) for x,y in zip(L1,L2)]
print((time.time()-start)*1000)
#5.46193122864

start = time.time()
result = A1+A2
print((time.time()-start)*1000)
#0.375032424927
'''
'''
a = np.array([(1,2,3,4),(4,5,6,7)])

print(a)
a = a.reshape(4,2)
print(a.size)
print(a)
print(a.itemsize)
print(a.shape)
print(a.dtype)
print(a.ndim)

a2 = np.linspace(1,3,10)
#Five element between 1 and 3 which are equaly spaced.
print(a2)
'''
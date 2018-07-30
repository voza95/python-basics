print("hello world by python!")  

num=5
#To get the address of variable
id(num)

#In Python if two variable have same value they will point to same addess(just like java).


#float division
print(8 / 4)

#int division
print(8 // 4)

print(2**3)

'''In terminal/IDLE 
the "sas" will output 'sas'
print("sas") will output sas
'''

print(10*'Jo..')

#\n mean new line

#to remove spiceal meaning start with r
print(r'c:\doc\navin')
#output will be c:\doc\navin

var name='youtube'

#Start from left to right
print(name[0])
#output: y

#Start from right to left
print(name[-1])
#e

print(name[0:2])
#yo

print(name[1:])
#outube

print(name[:4])
#yout

#string in python are immutable

len(name)
#7

#list which are mutable
nums=[19.8,77,'dfdf',33,99.99]

#insert add at perticular index
nums.insert(2,'ds')

#append add the element at the end of the list
nums.append(91)

#remove the element which is give if element not present then change nothing in list

#pop remove the element on index basies.
nums.pop(1)
#If no index/value is give to pop it remove the last element(it uses stack data strutre).

#To delete multiple values we use del
del nums[2:]
#Starting from second index delete all elements.


nums.extend([29,12,15.6,'dse'])

#Tuples are immutable
tup1 = (10,8,9,55) 

#Set is a collection of unique elements and it do not maintain insertion order
set1 ={22,25,14,21,5}
#5,14,21,22,25

set2={22,22,14,21,5,78,99}
#22,5,99,21,78,14
#Set store thing in randome values because set uses the concetp of hash with only improves performance.
#Indexing is not support because it don't have any.(cannot use set2[0])
#set mutable


#range
range(1,6)

#convertion
list(range(5))
#[0,1,2,3,4]

#list start from 2,ends at 10,at diffrence of 2
list(range(2,10,2))
#[2,4,6,8]

list(range(10,2,-2))
#[10, 8, 6, 4]

#Sequence is a data type which include list,tuple,set,string,range

#In Map/Dictionary for each value we provie a key(Key : vlaue)
#All the key has to be unique
temp={1:'hello',2:'yo',3:'Sup'}

#seach in map
#Starts with 1 not zero
temp[1]
#can use get method
temp.get(1)



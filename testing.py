
#foods = ['Jam','Chips','Bread','Cookies','Soda','Nachoies']    

#for x in foods[:2]:
#   print(x),
#   print(len(x))
#---------------------------------------
'''
for x in range(50,5,-4):
    print(x),
'''
#-----------------------------------------------
'''
print 'dsd',5

demo = 5

while(demo<52):
    print(demo),
    demo+=4
#test
for x in range(1,100):
    if( x%4 == 0):
        print(x)
'''
#-----------------function--------------------------
'''
def beef():
    print('Dume, Funtion')
    
def bittousd(bitcoin):
    amount = bitcoin * 7000
    print(amount)
    
beef()
bittousd(1.35)

#Return
def test(marks):    
   remain=100-marks
   return remain
   
lessthen = test(88)

print(lessthen)
#
def systype(sys = 'binary'):
    if(sys=='Quantum'):
        sys='1 and 0'
    elif(sys=='ternary'):
        sys='+tv,-tv or zero'
    else:
        sys='1 or 0'
    return sys

info = systype('Quantum')    

print(info)
'''
import modulefile

def dumstrint(a1='yellow',a2='gellow',a3='below'):
    '''This function greets to
	the person passed in as
	parameter'''
    print(a1 ,a2,a3)
    
dumstrint()
dumstrint(a3='dellow')
print(dumstrint.__doc__)

# Program to show the use of lambda functions
'''
double = lambda x: x * 2

# Output: 10
print(double(5))

number_list = [ x for x in range(20) if x % 2 == 0]
print(number_list)
'''
#to take multiple arguments we use */Flexible number argument
def add_numbers(*args):
    total = 0
    for a in args:
        total += a
    print(total)   

add_numbers(4,4)
add_numbers(4,8,5,3,7)
  
#Unpacking arguments
def unpackdemo(a1,a2,a3):
    print(a1+a2+a3)

listdemo=[12,51,0]

unpackdemo(*listdemo)

modulefile.first()


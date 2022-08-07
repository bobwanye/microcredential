"""
Pythonn and Postgresql exercises
Gavin Lowenfield
"""
import random

fruit_list =[]

nofruits = int(input("Enter the number of Fruits: "))

for i in range(nofruits):
    print("Enter the Fruit ",i+1,": ")
   
    fruit_item  = input()
    
    fruit_list.append(fruit_item)

print("The user created a list of {0} items and entered the values : {1}".format(nofruits,fruit_list))
#activity B
n1=int(input("Enter first number >> "))
n2=int(input("Enter second number >> "))

i=0
large=0

if n1>n2:
    i=n2
    large=n1
else:
    i=n1
    large=n2

while(i<=large):
    print(i)
    i=i+1
#activity C
    from math import pi
def cylinder_volume(r, h):
 return pi*r**2*h

r=float(input('Enter radius of the cylinder: '))
h=float(input('Enter height of the cylinder: '))
print('Volume of the cylinder: {:g}'.format(cylinder_volume(r,h)))
#activity D

numRolls=int(input("How many times you want to roll?"))
for row in range(1, numRolls + 1):
    roll = 0
    roll+= 1
    print(f"Roll {roll} = {random.randint(1,6)}")


    


    

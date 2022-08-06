"""
activity 19 functions
type your name
"""
import math
import random
# example 8) pass statement
def filter_num():
    pass

# example 7) boolean functions
def is_divisible(x,y):
    if x%y == 0 or y%x == 0:
        return True
    else:
        return False
# example 6) def fucntion with parameters and return value
def sum(num1,num2):
    total = num1+num2
    return total

def number ():
    n1 = int(input("enter number 1:"))
    n2 = int(input("enter number 2:"))
    x = sum(n1,n2)
    print("The sum of %s and %s is %s" %(n1,n2,x))
#example 5 defined function with parameter and no return value
def country(c="Norway"):
    print("----EXAMPLE 5-----")
    print("I am from %s" %(c))

#example 4 defined function with parameter and no return value
def name(fname):
    print("------example 4------")
    print("welcome to the program %s" %(fname))
# example 3) defined function: no parameter nor return value
def my_function():
    print("----EXAMPLE 3----")
    print("Hello from a fuction\n")
    
#example 2) random numbers.Ramdomly pick a color form the list
color =['red','blue','green']
randomIndex =random.randint(0,2)
print(randomIndex)
print("The picked color is %s" %(color[randomIndex]))
# example 1 using built in
radius = float(input("enter a rdius"))
circumference = 2*math.pi*radius
circumference = round(circumference, 2)
area = math.floor(math.pow(radius,2)*math.pi)
print("the circumfrence with radius %s is %s and the area is %s" %(radius,circumference,area))

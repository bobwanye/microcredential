"""
Gavin Lowenfield Activity 18
8/3/2022
"""
print("\n\n------- ACTIVITY 18--------")

print("\n\n------- WHILE LOOP--------")
print("example 15 ask user to enter two numbers between 0 and 10 with checkpoint. Use a while loop to increment each number by 2 until the sum of them reach up to 30")
number1 = int(input("Enter a number between 0 and 10:"))
while number1<0 or number1>10:
    number1=int(input("try again enter a number between 0 and 10:"))

number2 = int(input("Enter a 2ndnumber between 0 and 10:"))
while number2<0 or number2>10:
    number1=int(input("try again enter a number between 0 and 10:"))

while number1<20 and number2<=20:
    addition = number1+number2
    print("%s + %s = %s" %(number1, number2, addition))
    break
    number1 += 2
    number2 += 2
    

print("example 14 create a while loop that cheaks if an entered number is between 0 and 10")
number= int(input("enter a number between 0 and 10"))
while number<0 or number>10:
    nunber = int(input( "try again"))
    print("enter number =" , number)
print("example 13 user enters two number between 0 and 10 . Use while loop toincremment each number by 2 until both of them reach up to 20")
num1= int(input("enter a number between 0 and 10"))
num2= int(input("enter a number 2nd between 0 and 10"))
while num1<=20 and num2<=20:
    print("num 1 = %s and number 2 = %s" %(num1, num2))
    num1 += 2
    num2 += 2
print("example 12 while loop basic")
i = 0
while i < 6:
    print("i=", i)
    i+= 1
else:
    print("i is no longer less than 6")


print("\n\n------- FOR LOOP--------")
print("example 11) for- else statement")
for n in range(7):
    print(n)
else:
    print("DONE!")

print("example 10 use for loop to print num from 10 to 5 and skip numbers that are mutiple of 4")
for num in range(10,-5,-1):
    if num%4 == 0:
        continue
    print(num)
print("example 9 heating for loop and if statment")
for counter in range(10):
    print("now counting:",counter)
    if counter==5:
        break
    print("=*=*=*=*=*")
print("example 8) for loop in a string")
msg= "hello world!"
for m in msg:
    print("characters= ", m)
print("example 7 for loop in a list")
colors=['yellow','red','blue','green','white','black']
for c in colors:
    print("color = ", c)
print("example6 for loop decerment counting:")
for z in range(20, -10, -5):
    print("z = ", z)
print("example5 for loop with three arguments:")
for y in range(2,30,2):
    print(" y = ", y)
print("example4 for loop basics:")
for x in range(0,5):
    print("counting:", x)

print("\n\n------ CONDITIONAL STATEMENT-----")
# Example 3) and or operators
age = int(input("enter an age"))
gender = input("type M for male or F for female")
if age == 5 and gender =="M" or gender=="m":
    print("5 year old boy")
elif age == 5 and gender =="F" or gender=="f":
    print("5 year old girl")




#if else if statement(example2)
age = int(input("Enter an age:"))
if age == 5:
    print("age = 5 Height should be around 102 cm and 14.8lbs")
elif age ==6:
    print("age = 6 Height should be around 108 cm and 16.3lbs")
elif age ==7:
    print("age = 7 Height should be around 113cm and 18.0lbs")
else:
    print("unable to display height and weight")

#if statement , example 1) check if an age is an adult
age = int(input("Enter an age: "))
if age>=21:
    print("you are an adult")
else:
    print("You are underage")
    print("welcome to the club")

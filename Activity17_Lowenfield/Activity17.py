#gavin Lowenfield - ACTIVITY 17
"""
mutiple
line
comment
"""
#list
fruits=["apples","oranges", "grapes","bananas", "pears", "cherries","mangos"]
print(fruits)
copyFruits= fruits.copy()
copyFruits.reverse()
copyFruits.append("grapes")
print("original list %s \n copy list %s" %(fruits,copyFruits))
numGrapes = copyFruits.count("grapes")
numKiwi = copyFruits.count("kiwis")
indexPears = fruits.index('pears')
print("There are" , numGrapes,"grape in  the list")
print("There are ",numKiwi,"kiwis in the list")
print("Pears has index", indexPears)

        

#string
msg = input("enter a message:")
fullName = input("Enter a full name:")
print( "%s Welcome %s" %(msg,fullName))
nameLen= len(fullName)
lastCharName = fullName[nameLen-1]
index_a=fullName.find("a")
print("Name %s has %s characters abd the last character is %s " % (fullName.upper(),nameLen,lastCharName))
print("name %s has index  A  with index %s" %(fullName, index_a))

print("Hello World Python")
# variables
number1 = -36
number2 = 10
addition = number1 + number2
name = "type your name"
character = 't'
#input for later
no_yes = False
print("Number 1 = ", number1)
#input() function
firstName = input("Enter a name:")
print("Hi,", firstName, "welcome to the party")
#string to int
num1 = input("Enter a number:")
num1 = int(num1)
num2 = int(input("Enter a second number:"))
prod = num1*num2
print(num1, "X", num2, "=", prod)
# exaple 3 hypotenuse of right angle
h= float(input("enter the height"))
w=  float(input("enter the width"))

hyp = (h*2+w**2)**0.5
print("The hypotenuse is:", hyp)

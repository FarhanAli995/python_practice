#day4:

# print("hellow world", 7)
# print(7)
# print(17127*35343)

#day5:

"""
please donot remove this line.
auther is fahan
 this is a 100 days course
you can use cntrl + / to convert all selected items into comments
""" 
# print("hey!I am a good boy\n "
# "and the viewer is also a good boy\n"
# "and this is 100 days course")   
# print("hi", 6, 7,sep="|",end="009\n") 
# print("farhan")
# print("wow", 8, 9, sep="~", end="009\n")
# print("harry")

# #day6:

# print(5 > 3)   # Output: True
# print(5 == 3)  # Output: False

# Logical operations

# print(True and False)  # Output: False
# print(True or False)   # Output: True
# print(not True) 

#day6:

# a = 19
# b = 18 
# d = "farhan"
# c = a + b
# print("19 + 18 =", c )
# print(a)
# print("the type of a is" , type(a))
# print("the type of b is " , type(b))
# print("the type of c is" , type(c))
# print(d)
# print("the type of d is " , type(d))
#here is list: collection different data types
#list is mutable
# list1 = [8,6.3,[-3,6],["apple", "mango"]]
# print(list1)

#here is dictionary:
#map data which is used to map one to another

# dict1 = {"name":"farhan" , "age":"22" , "single":"true"}
# print(dict1)

#here is tuple:
#the only difference b/w tuple and list is tha tuple is immutable
# tuple1 = (("parrot" , "sparrow") , ("lion" , "tiger"))
# print(tuple1)

# print(5 > 3)   # Output: True
# print(5 == 3)  # Output: False

# Logical operations

# print(True and False)  # Output: False
# print(True or False)   # Output: True
# print(not True)  

#everything is an object in python

#day7:

#Arithemetic operators

# print(15 + 6)
# print(15 - 6)
# print(15 * 6)
# print(15 / 6)
#floor division
# print(15 // 6)
#remainder
# print(15 % 6)
#exponential
# print(15 ** 6)

#day8:

# name1 = 'farhan'
# name2 = "farhan"
# name3 = '''farhan'''
# a = None

# print(name1)
# print(name2)
# print(name3)
# print(a)

#day9:

#reserved word in python:
"""
and
as
else
assert
break
class
continue
def
del
elif
esle
except
finally
False
for
from
global
if
import
in
is
lambda
nonlocal
None
not
or
pass
raise
return
True
try
with
while
yeild

> we can't use these words as name any variable.
> pyton is a case senstive language
> e.g in python small(a) and capital (A) is a different variable.

"""

#types of tokens:
"""
punctuators are symbols to organise the sentebce structure in programming.
e.g 1_()
> parantheisis 
> like we can code a*b+c or we can use parantheises (a*b)+c to make it better

e.g 2_{},[]
> we study thse curly and square brackets during studying tuples,lists,and dictionaries.

@,{},[],# etc
> these all are also examples of punctuators 

TYPES OF LANGUGES:
1.IMPLICITE:
those in which don't need to declaire type variable of langauges like python 
e.g.
num1=5
print("num1 = ",num1)

2.EXPLICITE:
In which we need declaire type of variable like c++
e.g
int num1;
num = 5;
cout<<"num1 = "num1;

"""
# expression excution:
# > strings & numeric values can operate togather with *
#we can (+,-,/,*) in string and numeric values
# a , b = 2 , 3
# text = "@"
# print(2 * text * 3)

# > string & and string can operate togather known as concatination
# > we can add string and string but can not (*,/,-,)
# f , g = "2" , 3
# txt = "@"

# print((f + txt) * g)

# > numeric values can operate with all arithmetic operators
#e.g
# r , h = 3 , 4
# dg = 6
# print(r + h * dg)

# arithemetic expression with integer and float will result in float
#we can use + * / - %  ** in these last two expressions

# sa , fa, = 2434 , 33434.3434
# print(sa * fa)

#day10:
#integer division with float and int will give int display as float
#e.g

# aa , ds = 1.5 , 3
# sd = aa// ds
# print(sd , aa / ds )
# print(sd , aa // ds )



#day10:
#floor gives closest integer, which is lesser than or equal to the float to float value
# result if (A // B)is same as floor (A / B)

"""

A , B = 12 , 5
c = A // B
print(A // B)

A , B = -12, 5
c = A // B
print(c)

A , B = 12, -5
c = A // B
print(c)
"""

"""
- / + = +ve
- / - = +ve 
+ / - = -Ve
- / + = +ve

"""


"""

av , bv = 5 , -13
cv = av % bv 
print(cv)

av , bv = 5 , -13
cv = av / bv 
print(cv)

"""

#input:

#string input:
"""
dd = "diyan"
name22 = input("name :")
print("hello" , dd)

#int input:

age = int(input("age "))

if age < 18:
    print("you are not capable for this test") 

elif age > 18 and age < 30  :
    print("you are capable for this test")

elif age > 30:
    print("you are not capable for this entry test")

name33 = input("name : ")
age = int(input("age : "))
grade = int(input("grade : "))

print("My name is " , name33 , "I am " , age , "years old" , "And I am in grade" , grade  )
"""
#day11:
 #conditional statements:

"""
if(condition) :
statement1

elif(condition) : 
statement
else : 
statementN

"""
#are able of voting:
"""
age = int(input("enter your age: "))

if age < 18:
    print("your are not able for voting :")
elif age > 18:
    print("you are able of voting:")
else:
    print("invalid error !")
"""
"""

light = input("enter color of traffic light:")

if (light == "green"):
 print("go!")
elif(light == "red"):
 print("stop!")
elif(light == "yellow"):
 print("look!")
elif(light != "green" and light != "red" and light != "red"):
 print("invalid error!")

"""

 #we can also use else: then statement here
"""

ac = int(input("A : "))
cc = input("M/F : ")

if((ac == 1 or ac == 2) and cc == "M"):
 print("fee is 100")

elif(ac == 3 or ac == 4 or cc == " F"):
 print("fee is 200")

elif(ac == 5 and cc == "M"):
 print("fee is 300")
else:
 print("No fee!")

 """
#single line if/ternary operator:
"""
food = input("food :")
eat = "yes" if food == "cake" else "no"
print(eat)

"""
#day12:

# clever if/ternary operator
# <var>=(false_val,true_val)[<condition>]
"""
age1 = int(input("enter age: "))
vote = ("Yes" , "No") [age1 < 18]
print(vote) 

"""

"""

salary = float(input("enter employee's salary: "))
tax = salary * (0.1 , 0.2) [salary <= 50000] 
print(tax)"

"""
#calculate interest:

# amount = float(input("enter principal/amount: \n"))
# rate = float(input("enter rate of intrest: \n"))
# time = float(input("enter time: \n"))
# intrest = (amount * rate * time / 100)
# print(intrest)

# Here is the extracted text from the image:

# --------------------------------------------------------------------------------------------------#

# **Types of Operators**  

# An operator is a symbol that performs a certain operation between operands.  

# - **Arithmetic Operators** (., -, *, /, %, **)  
# - **Relational / Comparison Operators** (=, !=, >, <, >=, <=)  
# - **Assignment Operators** (=, -=, *=, /=, %=, **=)  
# - **Logical Operators** (not, and, or)  

# --- 

# Note: Some symbols in the original image appear unclear or possibly incorrect 
# (e.g., `.` in Arithmetic Operators, `-=` repeated in Assignment Operators). 
# The extracted text reflects the content as shown.


#assignment operators:
# numm = float(input("enter num: "))
# numm += 10
# print(numm)

# numm -= 10
# print(numm)

# numm *= 10
# print(numm)

# numm /= 10
# print(numm)

# numm **= 10
# print(numm)

#day13:

# yourName = input("enter your name: ")
# print("ye thu gor",yourName)
 
# nn = float(input("enter a value:"))
# print(type(nn),nn)12

# SideSquare = float(input("enter Square side length:"))
# print("The square of square is",SideSquare * SideSquare)

# num1 = float(input("enter first number:"))
# num2 = float(input("enter second number:"))
# c = num1 + num2 / 2
# print(c)
 
# dd = float(input("enter 1st number:"))
# ds = float(input("enter 2nd number:"))
# print(dd >= ds)
# or
# if(dd > ds):
#     print(True)
# else:
#     print(False)


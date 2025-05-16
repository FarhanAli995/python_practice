#NEW CHAPTER{STRINGS}:

"""
>DEF: Strings is data type that stores a sequence of characters.
>CONCATINATION:Adding two strings.
>e.g "hello" + "world"       > "helloworld"

"""
# e.g of concatination:

"""

str1 = "hello "
len1 = len(str1)
print(len1)

str2 = "farhan"
len2 = len(str2)
print(len2)

addString = str1 + str2
len3 =len(addString)
print(len3)
print(addString)

"""

#day14

# Indexing 
# -------------------- 
# index → position  

# Appa_College  
# 0 1 2 3 4 5 6 7 8 9 10 11  

# str = "Appa_College"  

# str[0] is 'A', str[1] is 'p' ...  

# str[0] = 'B' #not allowed

# access  
# str[2]
"""

Indexing  
index → position  

Appa_College  
0 1 2 3 4 5 6 7 8 9 10 11  

str = "Appa_College"  

str[0] is 'A', str[1] is 'p' ...  

str[0] = 'B' #not allowed

access  
str[2]
"""

### Explanation:
# 1. The image explains string indexing, showing how each character in the string `"Appa_College"` corresponds to an index position (0 to 11).
# 2. It demonstrates accessing characters using indices, e.g., `str[0]` is `'A'`, `str[1]` is `'p'`, etc.
# 3. It notes that modifying a character directly (e.g., `str[0] = 'B'`) is not allowed in Python, as strings are immutable.
# 4. The last line shows how to access a specific character (`str[2]`).

"""

MyName = "farhan"
ch = MyName[0]
print(ch)

ch = MyName[1]
print(ch)

ch = MyName[2]
print(ch)

ch = MyName[3]
print(ch)

ch = MyName[4]
print(ch)

ch = MyName[5]
print(ch)

"""



# Slicing

## Accessing parts of a string

# str[ starting_idx : ending_idx ] #ending idx is not included  
# str = "ApnaCollege"  
# str[ 1 : 4 ] is "pna"  
# str[ : 4 ] is same as str[ 0 : 4 ]  
# str[ 1 : ] is same as str[ 1 : len(str) ]


### Explanation:
# 1. The image explains **string slicing** in Python, which allows accessing substrings.
# 2. Syntax: `str[starting_idx : ending_idx]`  
#    - The `ending_idx` is **not included** in the slice.
# 3. Example:  
#    - For `str = "ApnaCollege"`, `str[1:4]` returns `"pna"` (indices 1, 2, 3).
# 4. Omitted indices:  
#    - `str[:4]` is equivalent to `str[0:4]` (starts from the beginning).  
#    - `str[1:]` is equivalent to `str[1:len(str)]` (goes until the end).

# name = "farhan"
# print(name[1:4])
"""
# String Slicing with Negative Indices
# Negative Indexing Example
# For the string:

# python
# Copy
# str = "Apple"
# Negative Indices:
# Copy
# A   p   p   l   e
# -5 -4 -3 -2 -1
# Slicing Example:
# python
# Copy
# str[-3:-1]  # returns "pl" (characters at indices -3 and -2)
# Note: The original image contained a typo showing the result as "pi", but the correct output for str[-3:-1] on "Apple" is "pl".

"""

# String Functions
#  str = “I am a coder.”
#  str.endsWith(“er.“)  #returns true if string ends with substr 
# str.capitalize( )  #capitalizes 1st char 
# str.replace( old, new )  #replaces all occurrences of old with new 
# str.find( word )  #returns 1st index of 1st occurrence 
# Apna College
#  str.count(“am“)  #counts the occurrence of substr in string

# cah = "i am a programmer"
#this code efect only for once the string in program

# print(cah.capitalize())
# print(cah.endswith("dfd"))
# print(cah.endswith("mer"))

#his code effect forever the string in program
# cah = cah.capitalize() , cah.endswith("dfd") , print(cah.endswith("mer"))
# print(cah)
# print(cah.replace("programmer" , "coder"))


#----------------------------------------------------------------------------------------------------------------------------------------------------
#DAY15:


###Conditional Statments:###

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
#TAKE REFERENCE OF DAY12:

# clever if/ternary operator
# <var>=(false_val,true_val)[<condition>]
"""
age1 = int(input("enter age: "))
vote = ("Yes" , "No") [age1 < 18]
print(vote) 

"""

#NESTING CODITIONS:
#syntax of nesting conditions:

# if(first_condition):
#     if(condtion inside first_codtion):
#         print(statemen of condtion inside first_codtion)
#     else:
#         print(statment of first condition)
        
#         after these there will other 
#     elif (coditions):
# their statements
  
'''

age = int(input("Enter your age: "))
if(age >= 18):
    if (age >= 80):
        print("-> you can't drive!")
    else:
        print("-> you can drive")

elif(age < 18):
    print("-> you can't drive")
else:
    print("invalid error!")
    
'''
##LETS PRACTICE:
# Q1. WAP  to find the greatest of 3 numbers entered by the user.
'''
Ans1:
num1 = float(input("-> Enter your first number:\n" ))
num2 = float(input("-> Enter your second number:\n"))
num3 = float(input("-> Enter your third number: \n"))

if(num1 > num2 and num1 > num3):
    print("num1 is greater than all" , num1)

elif(num2 > num1 and num2 > num3):
    print("num2 is greater than all" , num2)

elif(num3 > num1 and num3 > num2):
    print("num3 is greater than all" , num3) 
else:
    print("Invalid Error !")  
'''
    
# Q2.WAP to check if a number is a multiple of 7 or not.

'''
Ans2:
num1 = float(input("Enter a number: \n"))

num2 = num1 % 7 

if(num2 == 0):
    print("The input number is multiple of 7")

else:
    print("The input number is not a multiple of 7")

'''



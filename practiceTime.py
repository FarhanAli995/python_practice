import UnipracticalClasses


# Q1. String Functions:
# Given s = "hello world", write code to:
# a) Capitalize the first letter.
# b) Replace "world" with "Python".
# c) Count occurrences of the letter "l".

'''
Ans1. s = "hello world"
print(s.capitalize())
print(s.replace("world" , "python"))
print(s.count("l"))'
'''

# Q2. Conditional Statements
# Grade Calculator:
# Write a program to assign grades based on marks:
# A (≥90), B (80-89), C (70-79), D (<70).
# Input: marks = 85 → Output: "B".

'''
Ans2.
marks= float(input("Enter Your Marks: "))

if marks >= 90:
    print("Congartes Your are passed \n your have got A grade")

elif marks >= 80:
    print("wow!you have got B grade \n you are passed")
    
elif marks >= 70:
    print("You have got c grade \n You are passed.")

elif marks < 70:
    print("Your grade is D , You are failed \n best of luck for next time.")

else:
    print("Invalid Error !")
    '''

#Q3 Odd/Even Check:
# Write a program to check if a user-input number is odd or even using if-else.

'''
Ans3. num1 = float(input("enter your first number: \n"))
num2 = float(input("enter your second number: \n"))

c = num1 % num2
print(c)

if c == 0:
    print("this is an even number")

elif c != 0:
    print("this is an odd number")

else:
    print("invalid error !")

'''

# Q4. Average Calculator:
# WAP to input 2 floating-point numbers and print their average.
'''
Ans4. num0 = float(input("enter num1:\n"))
num1 = float(input("enter num2:\n"))
num2 = float(input("enter num3:\n"))
num3 = float(input("enter num4:\n"))
num4 = float(input("enter num5:\n"))

d = num0 + num1 + num2 + num3 + num4 / 5
print(":> average = sum of all input values and divided by number of input values ")
print("(num1) x num2 x num3 x num4 x num5 / 5 =" , d)
                  
'''

# Q5. Advanced String Problems:
# Substring Occurrence:  
# WAP to count how many times "`$`" appears in a user-input string.  
#    Example: `"a$b$c"` → Output: `2`.
'''
# a= "a$b$c"

#counting:
# b = a.count('$')
# print(b)

#length finding:
# length_a = len(a)
# print(length_a)

#indexing:
# indexing_a = a[3]
# print(indexing_a)

#slicing:
# c = a[2:5]
# print(c)

'''


def show(self):
        print(self.reg_no , self.name)

s1 = Student(101 , "farhan")
s1.show()
print("__________")
s2 = Student(2322, "alsihan")
s2.show()
print("___________")



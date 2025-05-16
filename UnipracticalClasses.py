
"""
a,b,c=1,4,"Hussain"
print(a,b,c)

list=['abcd',786,2.23,'john',70.2]
print(list)
print(list*4)

Mylist=[1,"sajid",87.8]
print (Mylist[1:]+list:1*10)
print("please enter a number")
i=input("number")
n=0
while(n<10):
n="n+1"

a, b, c = 1, 4, "Hussain"
print(a, b, c)

# Correct list operations
my_list = ['abcd', 786, 2.23, 'john', 70.2]
print(my_list)
print(my_list * 4)

# Corrected list slicing and concatenation
another_list = [1, "sajid", 87.8]
print(another_list[1:] + another_list[:1] * 10)

# Corrected while loop with proper indentation
print("Please enter a number")
i = int(input("number: "))  # Convert input to integer
n = 0
while n < 10:
    n = n + 1
    print(n)  # Print the value of n in each iteration


print(5 > 3)   # Output: True
print(5 == 3)  # Output: False

# Logical operations

print(True and False)  # Output: False
print(True or False)   # Output: True
print(not True) 
"""
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
# #here is list: collection different data types
# #list is mutable
# list1 = [8,6.3,[-3,6],["apple", "mango"]]
# print(list1)

# #here is dictionary:
# dict1 = {"name":"farhan" , "age":"22" , "single":"true"}
# print(dict1)

# #here is tuple:
# #the only difference b/w tuple and list is tha tuple is immutable
# tuple1 = (("parrot" , "sparrow") , ("lion" , "tiger"))
# print(tuple1)

# ###class2:###

# for x in range (1,1000):
#     print(x)

# list = [1 , 2 , 3 , 4 , "alishan"]  # i  in this code means index
# for i in list:
#     print(i)

# sum = 0
# for i in range(1, 111):
#     sum = sum + (i * i)
#     print(sum)


# integer = int(input("eneter a number: "))
# factorial = 1
# for i in range(1, integer + 1):
#     factorial *= i

# print(f"The factorial of {integer} is {factorial}")

# while loop syntax:


#module, package:
#Class:
# class Class01:
#     def __init__(self):
#         print("just created an object for class01")
        
# class Class02:
#     def __init__(self):
#               print("just created an object for class02")



# c1 = Class01()
# c2 = Class02()

# class Stu:
#       x = 0
#       y = 2
#       def show(self , x , y):
#             print(x, y)

# s1 = Stu()
# s2 = Stu()
# print(s1.x , s2.y)

# class Student:
#     sem = "2nd"
#     def __init__(self ,reg_no,name):
#         self.reg_no = reg_no
#         self.name = name
    
#     def show(self):
#         print(self.reg_no , self.name)

# s1 = Student(101 , "farhan")
# s1.show()
# print("__________")

# s2 = Student(2322, "alsihan")
# s2.show()
# print("___________")

# s3 = Student(2322, "diyan")
# s3.show()
# print("___________")

# # ✅ Move this line inside the loop

#Q1: print numbers from 1 to 100.

# num1 = 1
# while num1 <= 100:
#     print(num1)
#     num1 += 1

#Q2: print the multiplication table of a number n?

# num2 = int(input("Enter your number:"))
# num3 =1

# while num3 <= 100:
#     print(f"{num2} x {num3} = {num2 *num3}")
#     num3 += 1


###FOR LOOP####
# vegetable = ["potato", "ladyfinger", "cucumber", "oninion"]
# for val in vegetable:
#     print(val)


###range###
# for el in range(1, 5, 2):
#     print(el)

# print("__________________________________")

# for el in range(1, 5):
#     print(el)

# print("__________________________________")
# for el in range(1 , 100, 3):
#     print(el)

###PASS###
# for i in range(12):
#     pass
# print("some useful work!")


##################################################################################

# i = len("anaconda")
# print(i)
# i = len([1, 2, 3, 4, 3, 3, 3, 3])

# print(i)



#...................................................................................................#

# class A:
#     def method01(self, a =None):
#         if a == None:
#             print("sequence 01")
#         else:
#             print("sequence 02")

# # class B(A):
# #     def f(self, i = None):


# def main():
#     a = A()
#     a.method01()
#     a.method01(3)

# if __name__=="__main__":
#     main()



#.......................................................................................................#

class Pet():
    def __init__(self, name1, age1):
        # super().__init__(name1, age1)

        class Dog(Pet):
         def __init__(self, name1, age1, breed1):
        # super().__init__(name1, age1)
             self.breed1 = breed1
    

    def Bark(self):
        print("bark bark")

class Cat(Pet):
    def Pur(self):
        print("pur pur")

spotty = Dog("spotty", 3, "Golden Retriever")
cutie = Cat("cuttie", 4)

spotty.Bark()
cutie.Pur()
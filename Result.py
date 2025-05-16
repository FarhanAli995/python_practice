# Recursion Method:
'''
def Show(n):
    if n == -5:
        return
    print(n)
    Show(n-1)

Show(10)
Show(5)
'''
"""
class Stu:
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    marks = float(input("Enter your marks: "))

s1 = Stu()
print(f"Students name is {s1.name} his, age is {s1.age} and his marks are{s1.marks}")          
"""
"""
class cars:
    colour = "red"
    brand = "BMW"
    model = "X5"
    year = 2020
c1 = cars()
print(f"car's colour is {c1.colour},it's{c1.brand}, it's model is {c1.model} and it's year is {c1.year}")
"""
"""
class Student:
    def __init__(self,name, age, marks):
        print("Constructor is called")
        self.name = name
        self.age = age
        self.marks = marks


s1 = Student("ALI",23,32)
print(s1.name,s1.age,s1.marks)

s2 = Student("AHMED", 25, 45)
print(s2.name,s2.age,s2.marks)

s3 = Student("TARIQ", 30, 50)       
print(s3.name,s3.age,s3.marks)

"""
# hello world


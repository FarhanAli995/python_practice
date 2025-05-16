# OOPs in python:
# to map the real world scenarios,we started using objects in Code
 
#Class & Objects in python:
#Class is a blueprint for creating objects.

#creating class:
"""
Summary
This YouTube video transcript explains the importance of classes and objects in Python programming. The speaker discusses how attributes defined inside a function can be accessed through a self-reference parameter, similar to accessing class variables directly from the class name or an object. The concept of calling functions from objects and passing values is also covered.

KeyPoints
📚 Classes are logical entities that contain code.
👥 Objects are instances of classes with their own attributes.
💡 Attributes can be accessed through self-reference parameters in functions.
🔄 Functions can be called from objects to access documentation strings.
📝 Documentation strings should be written at the beginning of a function.
🕒 Constructors can automatically call functions with default values.
💻 Dynamic typing allows variables to be identified and sized at runtime.

Analogy
Creating a class is like building a house. The blueprint (class) defines the structure, while the actual house (object) has its own unique features and attributes.

Important Keywords and Definitions
· Class: A logical entity that contains code.
· Object: An instance of a class with its own attributes.
· Self-reference parameter: A way to access attributes defined inside a function from within the function.
· Constructor: A special function that gets called automatically when an object is created, used to set default values for attributes.
· Dynamic typing: The ability of a programming language (like Python) to identify and size variables at runtime, rather than at compile time.
. with the help of constructor(__init__) we can call the variables of class multiple times in class but in procedural programming we need to write that code again and to again recall tha value of variable.
(self) is a reference to the current instance(object) of the class.

"""
"""
class Stu:
    name = "farhan aly"
"""
#creating objects (instance)
"""
s1 = Stu()
print(s1.name)

class A:
    def __init__(self):
        print("Constructor is called")
        self.name = "farhan"
        self.age = 22
        self.city = "Gilgit"
        self.country = "Pakistan"
obj = A()
print(obj.name)
print(obj.age)
print(obj.city)
print(obj.country)

"""
class Aa:
    """learn python
    this is a class"""
    age = 22
    def fun(self):
        name = "fahan"
        print(name)
        
   
obj1 = Aa()
print(obj1.__doc__)
print(obj1.age)
print(obj1.fun())

# We don't need call the constructor explicitly, it will be called automatically when we create an object of the class.
# The constructor is a special method that is called when an object is created. It is used to initialize the attributes of the object.



###DAY16###

##LISTS IN PYTHON:
'''
->def: 1. A build-in data type that stores set of values.
2. It can store elements of d/f Types(int,float,string,etc)

->e.g
1. marks = [23, 42 , 234, 242, 45]    # marks[0], marks[1],.....
2. student = ["farhan"  , 343 , "delhi"] #student[0], student[1],....
'''
# marks = [23.3 , 45.5 , 42.4 , 34.34 , 76.34 , 92.3 ]
# print(marks)


# print(marks[0])
# print(marks[1])
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# marks_len = len(marks)
# print(marks_len)

#main d/f betwween string and lists is that:

'''
-> strings are immutable
-> list are mutable
e.g 
-> marks[0] = "alishan"
print(marks[0])

-> name = input("enter your name: \n")
name_indx = name[-1 : -20 : -1]
print(name_indx)

'''
###DAY17###

#LIST METHODS:

# scores = [132, 423, 32, 323, 422]
# score_index = scores[-1 : -8 : -1]
# print(score_index)

# score_len = len(scores) 
# print(score_len)

# #append:

# scores.append(9)
# print(scores)

# #sort:

# scores.sort()
# print(scores.sort())

# #reverse sort:

# scores.sort(reverse = True)
# print(scores)

# remove method:

# scores.remove(423)
# print(scores)

# pop method:

# scores.pop(2)
# print(scores)


#TUPLES:
'''

# Tuples in Python

A built-in data type that lets us create immutable sequences of values.

tup = (87, 64, 33, 95, 76)  
#tup[0], tup[1]...

tup[0] = 43  
#NOT allowed in python  

tup1 = ( )  
tup2 = ( 1, )  
tup3 = ( 1, 2, 3 )
```

### Key Notes from the Content:
1. **Tuples** are **immutable** (cannot be modified after creation).  
2. Syntax examples:  
   - Empty tuple: `tup1 = ()`  
   - Single-element tuple (requires a comma): `tup2 = (1,)`  
   - Multi-element tuple: `tup3 = (1, 2, 3)`  
3. Attempting to modify a tuple (e.g., `tup[0] = 43`) raises an error.  

Let me know if you'd like further explanation!

'''

'''
# examples of tuples:
scores = (132, 423, 32, 323, 422)
print(scores)
print(type(scores))
slicing_score = scores[0 : 4]
print(slicing_score)

'''
'''
# methods of Tuples:

scores = (132, 423, 32, 323, 423)   
print(scores)

#1. TUPLES COUNT:

scores_count = scores.count(423)
print(scores_count) 
                 #Or
print(scores.count(423))

#2. TUPLES INDEX:

scores_index = scores.index(423)
print(scores_index)
'''
#LETS PRACTICE:

#Q1. WAP to ask the user to enter names of their 3 favorite movies and store them as a list.

'''

movie1 = input("Enter your first favorite movie name: ")
movie2 = input("Enter your second favorite movie name: ")
movie3 = input("Enter your third favorite movie name: ")

movies_list = [movie1, movie2, movie3]
print(movies_list)

'''

'''
better response:

movies = []  
for i in range(3):  
    movie = input(f"Enter your {i+1} favorite movie name: ")  
    movies.append(movie)  

print(movies)
'''
#Q2. WAP to check if a list contains a palindrome of a elements.(Hint use copy() method

print("This below list is not palandromic: \n")

list1 = [1, 2, 3]
list1.copy()
print(list1)

list1.reverse()
print(list1, "\n")

print("This below list is palandromic: \n")

list2 = [1, 2, 3, 2 ,1]
list2.copy()
print(list2)

list2.reverse()
print(list2)

print(list2[-1 : 0 : -1])




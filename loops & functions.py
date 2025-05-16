# def cal_sum(a , b):
#     sum = a + b
#     print(sum)
#     return a + b
# cal_sum(12 , 23)
# cal_sum(23, 323)

# #OR

# def cal_add(a, b):
#     return a + b

# sum1 = cal_add(1, 2)
# print(sum1)

# Average of 3 nums:

def cal_average(aa, bb, cc):
    average = aa * bb * cc / 3
    print(average)
    return  aa * bb * cc / 3

cal_average(23, 23, 23)
cal_average(43, 34, 65)

class stu:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

farhan = stu("Farhan Ali", 12)
harry = stu("harry", 11)

print(f"My name is {farhan.name} & I am in class {farhan.grade}")
print(f"My name is {harry.name} & I am in class {harry.grade}")


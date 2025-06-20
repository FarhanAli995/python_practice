#Here def get_val and etc methods are called nonStatic methods or we
#say normal methods and def hell is nonStatic Method.

# Static Methods:
#  Methods that don’t use the self parameter (work at class level)
#  ge” )
#  #decorator
#  *Decorators allow us to wrap another function in order to
#  extend the behaviour of the wrapped function, without
#  permanently modifying it



class Stu:
    def __init__(self,name,marks):
        self.marks = marks
        self.name = name
    @staticmethod
    def hell():
        print("hellow world:")

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print("hi",{self.name},"your avg score is:", {sum/3})



s1 = Stu("farhan", [99, 33, 34])
s1.get_avg()

s1.name = "alyyfarhan4"
s1.get_avg()

s1.hell()






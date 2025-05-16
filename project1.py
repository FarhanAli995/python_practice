class Pet:
    def __init__(self, name1, age1):
        self.name = name1
        self.age = age1

class Dog(Pet):
    def __init__(self, name1, age1, breed1):
        super().__init__(name1, age1)
        self.breed = breed1

    def Bark(self):
        print("bark bark")

class Cat(Pet):
    def Pur(self):
        print("pur pur")

spotty = Dog("spotty", 3, "Golden Retriever")
cutie = Cat("cutie", 4)

spotty.Bark()
cutie.Pur()

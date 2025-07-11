class Dog():
    def speak(self):
        print(self.name,"goes bark bark")

    def __init__(self,name):
        self.name = name

class Cat():
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name, "goes meow meow")

class Bird():
    def __init__(self,name):
        self.name = name

    def speak(self):
        print(self.name, "goes tweet tweet")

odog1 = Dog("Frank")
odog2 = Dog("Jay")
ocat1 = Cat("Tim")
ocat2 = Cat("Bill")
obird1 = Bird("Jack")
obird2 = Bird("Pauly")


pets = [odog1,odog2,ocat1,ocat2,obird1,obird2]

for pet in pets:
    pet.speak()
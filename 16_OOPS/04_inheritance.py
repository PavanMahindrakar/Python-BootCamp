#Inheritance in Python allows a class to inherit attributes and methods from another class, promoting code reuse and organization.
#Inheritance with method overriding #E.g 1
class animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("Speaking...")


class Dog1(animal):
    def speak(self):
        super().speak()  # Call the speak method of the parent class
        print(f"{self.name} is barking")
        print("woof!")


D = Dog1("Sheru")
D.speak()  # Output: woof!


#Inheritance with method overriding #E.g 2
class car:
    def __init__(self, name):
        self.name = name

    def drive(self):
        print("Driving...")

class electricCar(car):
    def drive(self):
        super().drive()
        print(f"{self.name} is driving silently")
        print("oeeeeeeee")

E = electricCar("Tesla")
E.drive()  # Output: Tesla is driving silently

#Constructor : it is a special method that is automatically called when an object of a class is created.
# It is used to initialize the attributes of the class.
# Constructor is defined using __init__ method.
# It can take parameters to set the initial state of the object.
class Emp:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

    def get_salary(self):
        return self.salary
    
    def info(self):
        print(f"The name of employee is {self.name}, salary is {self.salary}, and the age is {self.age}")

e1 = Emp("yug", (50000), 23)
e1.info()  # Output: The name of employee is yug, salary is 50000, and the age is 23
# print((e1.info()))
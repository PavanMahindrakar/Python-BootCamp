#dunder methods are special methods in Python that start and end with double underscores (__).
# They allow you to define the behavior of your objects for built-in operations like addition, string representation, etc.      
# Common dunder methods include __init__ (constructor), __str__ (string representation), and __repr__ (official string representation).
# Dunder methods are used to implement operator overloading, customize object behavior, and provide a more Pythonic interface for your classes.
class Employee:
    company = "TechCorp"  # Class variable

    def  __init__(self,name, salary):
        self.name = name  # Instance variable
        self.salary = salary

    def __str__(self):
        return f"the name of emp is {self.name} and the salary is {self.salary}"


    def __repr__(self):
        return f"name: {self.name}, salary: {self.salary}"
    
e = Employee("Alice", 50000)
print(e.name , e.salary)
print(str(e))  # Using __str__ method to get a string representation of the object
print(repr(e))  # Using __repr__ method to get a detailed representation of the object
#Class : class is a blueprint for creating objects
# It encapsulates data for the object and methods to manipulate that data.

#Object: # An instance of a class. It is created using the class blueprint.
# Attributes: Variables that belong to the class.
# Methods: Functions that belong to the class and can manipulate the object's data.



class Employee:
    company = "Google"

    def get_salary(self): #self is a reference to the current instance of the class     
        return 50000
    

e1 = Employee()
print(e1.company)  # Output: Google
print(e1.get_salary())  # Output: 50000

e2 = Employee()
print(e2.company)  # Output: Google
print(e2.get_salary())  # Output: 50000
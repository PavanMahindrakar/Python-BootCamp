class Employee:
    company = "TechCorp"  # Class variable

    def __init__(self, name, salary):
        self.name = name  # Instance variable
        self.salary = salary  # Instance variable

    # Instance method(default)
    def info(self):
        info = f"the name of emp is {self.name} and the salary is {self.salary}"
        print(info)

    # Static method
    @staticmethod
    def sum(a, b):
        return a + b
    
    # Class method
    @classmethod
    def get_company(cls):
        return cls.company
    
    @classmethod
    def change_company(cls, new_company):
        cls.company = new_company

e1 = Employee("Alice", 50000)
e2 = Employee("Bob", 60000)
e1.info()

print(e1.sum(10, 20))  # Calling static method using instance

print(e1.get_company())
e1.change_company("TCS")
print(e1.get_company())  # Calling class method using instance
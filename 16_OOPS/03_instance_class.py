#instance and class attributes
# Instance attributes are specific to each object, while class attributes are shared across all instances of the class.
# Instance attributes are defined within the __init__ method, while class attributes are defined directly within the class body.

# class attributes are shared by all instances of the class, while instance attributes are unique to each instance.  

class car:
    color = "Black"
    def __init__(self, name ,model, year, price, color):
        self.name= name
        self.model = model
        self.year=year
        self.price=price
        self.color=color

    def info(self):
        print(f"The name of the car is {self.name}, model is {self.model}, year is {self.year}, and the price is {self.price}")

c1 = car("BMW", "X5", 2023, 800000, "white")    
car.info(c1)  # Output: The name of the car is BMW, model is X5, year is 2023, and the price is 800000

# Accessing class attribute and instance attribute
print(c1.color)  # Output: white # Accessing instance attribute
print(car.color)  # Output: Black # Accessing class attribute
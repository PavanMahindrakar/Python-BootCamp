class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self,p):
        return Point((self.x + p.x), (self.y + p.y))
    
    def print_point(self):
        print(f"x is {self.x} and y is {self.y}")

    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))

p1 = Point(2, 3)
p2 = Point(4, 5)

#operator overloading allows us to use + operator for custom objects
# Instead of using the sum method, we can use the + operator    
# p3 = p1.sum(p2)
p3 = p1 + p2  # This will not work unless we define __add__ method
p3.print_point()  # Output: x is 6 and y is 8
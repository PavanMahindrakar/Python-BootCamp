x = 50  # This is a global variable, accessible throughout the module

def sum(a, b):
    print("This is a global function")
    c = a + b
    global x  # Declare x as a global variable
    x = 25 #this will refer to the global variable x
    
    return c

sum(10, 20)  # Output: 30
print(x)  
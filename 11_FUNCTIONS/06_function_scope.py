def sum(a, b): #a nd b are local variables .. these can be destroyed after function returns
    c = a + b
    x = 25 #it doesnt chanege the value of global x ...it just create another local variable named x
    return c

def greet():
    x = 99
    print("Hello, World!")  # This function has its own local scope


print(sum(10, 20))  # Output: 30
greet()  # Output: Hello, World!



x = 40 # x is a global variable .. this can be used in any function or anywhere in the program
print(x)  # Output: 40
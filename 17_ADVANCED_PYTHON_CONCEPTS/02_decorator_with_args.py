def repeat(n):
    def decorator(func):
        def wrapper(a):
            for i in range(n):
                func(a)
        return wrapper
    return decorator

@repeat(7)
def say_hello(name):
    print(f"Hello, {name}!")

say_hello("Alice")  # Output: Hello, Alice! (7 times)

'''
iterate this code:
def decorator(func):
    def wrapper(a):
        for i in range(n):
            say_hello(a)
    return wrapper
    
# This is equivalent to the @repeat(7) syntax above.
# The decorator function takes an argument n, which is the number of times to repeat the function call.
# '''
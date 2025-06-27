#decorators are a way to modify or enhance functions or methods without changing their code.
# Decorators are a powerful feature in Python that allows you to modify or enhance functions or methods without changing their code.

def decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()  # Output: Something is happening before the function is called. Hello! Something is happening after the function is called.

# f = decorator(say_hello)
# f()  # Output: Something is happening before the function is called. Hello! Something is happening after the function is called.

'''
f will look like this:
def f():
    print("Something is happening before the function is called.")
    say_hello()
    print("Something is happening after the function is called.")

# This is equivalent to the @decorator syntax above.
# '''
"""Lambda functions are small anonymous functions defined with the lambda keyword.
They can take any number of arguments but can only have one expression.
these are one line functions, which are used for short-term use.
"""

square = lambda x: x * x
'''this lambda function as good as following function:
def square(x):
    return x * x
'''
print(square(5))  # Output: 25

sum = lambda a, b: a +b
'''this lambda function as good as following function:
def sum(a, b):
    return a + b
'''

print(sum(10, 20))  # Output: 30


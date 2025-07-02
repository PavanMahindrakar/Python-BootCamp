from functools import reduce

numbers = [1, 2, 3, 4, 5]
#         [3, 3, 4, 5]
#         [6, 4, 5]
#         [10, 5]
#         [15]

def add(x, y):
    return x + y

# Using reduce to apply the add function cumulatively to the numbers list
# reduce() returns a single value, which is the result of applying the function cumulatively
new = reduce(add, numbers)
print(new)

# Using a lambda function to achieve the same result
new = reduce(lambda x, y: x + y, numbers)   
print(new)
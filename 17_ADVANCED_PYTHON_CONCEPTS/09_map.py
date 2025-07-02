numbers = [1,2,3,4,5]

def square(x):
    return x * x

# Using map to apply the square function to each element in the numbers list
# map() returns an iterator, so we convert it to a list
new = list(map(square, numbers))
print(new)

# Using a lambda function to achieve the same result
new = list(map(lambda x: x * x, numbers))   
print(new)
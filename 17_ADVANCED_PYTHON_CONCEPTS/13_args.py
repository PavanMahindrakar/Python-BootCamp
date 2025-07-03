# def sum(a,b):
    # return a + b

def sum(*args):
    #args is a tuple of all arguments passed to the function
    total = 0
    for num in args:
        total += num
    return total

print(sum(1,2))  # Output: 3
# print(sum(1,2,3))  # Output: TypeError: sum() takes 2 positional arguments but 3 were given

print(sum(1,2,3))  # Output: 6
print(sum(1,2,3,4))  # Output: 10
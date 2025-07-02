def is_grater_than_10(x):
    if x > 10:
        return True
    else:
        return False

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

# Using filter to get numbers greater than 10
# filter() returns an iterator, so we convert it to a list
new = list(filter(is_grater_than_10, numbers))
print(new)

# Using a lambda function to achieve the same result
new = list(filter(lambda x: x > 10, numbers))
print(new)
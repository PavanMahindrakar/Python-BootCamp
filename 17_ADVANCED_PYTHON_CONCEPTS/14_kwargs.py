def marks(**kwargs):
    # kwargs is dictonary with key value pairs whcih is passed to the function
    # kwargs is used to pass a variable number of keyword arguments to a function
    for item in kwargs.keys():
        print(f"the mark of {item} is {kwargs[item]}")

marks(jack=90, rahul=80, scify=85)  # Output: the mark of english is 90, the mark of math is 80, the mark of science is 85
def func(*args, **kwargs):
    print("Positional arguments:", args)
    print("Keyword arguments:", kwargs)


# Example usage
func(1, 2, 3, name="Alice", age=30)
# Output:   
# Positional arguments: (1, 2, 3)
# Keyword arguments: {'name': 'Alice', 'age': 30}
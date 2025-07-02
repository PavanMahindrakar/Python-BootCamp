#finally block is used to execute code regardless of whether an exception was raised or not.
# It is often used for cleanup actions, such as closing files or releasing resources.   
def divide(a,b):
    try:
        c = a / b
        print(f"The result of {a} divided by {b} is: {c}",c)
        return c
    
    except Exception as e:
        print(f"An error occurred: {e}",e)
        return None
    
    finally:
        print("Execution of the divide function is complete.")

a = int(input("Enter a number 1: "))
b = int(input("Enter a number 2: "))

result = divide(a, b)
print(result)
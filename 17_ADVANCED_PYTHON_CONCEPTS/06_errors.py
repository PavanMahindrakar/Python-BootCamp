#try and except are used to handle exceptions in Python.
# When an error occurs in the try block, the code in the except block is executed.
# This allows you to handle errors gracefully without crashing the program. 
while True:
    try:
        a = int(input("Enter a number 1 : "))
        b = int(input("Enter a number 2 : "))
        print((f"the division of {a} and {b} is : {a/b}"))

    except ValueError :
        print("Please don't perform bad typecast.")
     
    except ZeroDivisionError:
        print("Please don't divide by zero.")
 
    except Exception as e:
        print(f"An unexpected error occurred: {e}",e)

    
## Example of raising an exception
# This code will raise a ZeroDivisionError if the user tries to divide by zero.
# It is a good practice to handle such cases to avoid runtime errors.# However, if you want to raise an exception intentionally, you can do so like this:
a = int(input("Enter a number 1 : "))
b = int(input("Enter a number 2 : "))
if a == 0:
    raise ZeroDivisionError("You cannot divide by zero.")
print((f"the division of {a} and {b} is : {a/b}"))

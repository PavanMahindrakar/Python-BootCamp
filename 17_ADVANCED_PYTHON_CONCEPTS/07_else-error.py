#else block in try-except
# The `else` block in a try-except structure is executed if no exceptions are raised in the try block.
# It is useful for code that should run only when the try block is successful.# Example of using else in try-except
try :
    a = 345/10

except Exception as e:
    print(f"An error occurred: {e}",e)
    
else:
    print("No errors occurred, the code ran successfully.")
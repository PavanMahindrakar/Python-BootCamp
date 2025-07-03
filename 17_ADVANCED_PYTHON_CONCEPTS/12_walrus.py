# walrus operator (:=) allows you to assign a value to a variable as part of an expression.
# This can help reduce redundancy and improve readability in certain cases.

#ex. 1
def slow():
    print("Starting slow function...")
    print("Starting slow function...")
    print("Starting slow function...")
    print("Starting slow function...")
    print("Starting slow function...")
    return 50

# a =slow()
if((a:=slow()>10)):
    print(a)
else:
    print("it is not greater than 10")
    

#ex. 2
# data = input("Enter the data: ")

while(data:=(input("Enter the data: "))):
    if data == "exit":
        print("Exiting the loop.")
        break
      
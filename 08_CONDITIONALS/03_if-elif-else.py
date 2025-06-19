age=int(input("Enter your age: ")) #input from user

if age > 18:
    print("You can drive")
elif age == 18:
    print("You can drive with a learner's license")
elif age == 0:
    print("You are not born yet")
else:
    print("You cannot drive")
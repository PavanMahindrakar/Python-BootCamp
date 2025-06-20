#String Formatting

template = "Hello, my name is {} and I am {} years old."
a = "Pavan"
a1 = 23

b = "Virat"
b1 = 37

s1 = template.format(b, b1)
print(s1)  # Output: "Hello, my name is Pavan and I am 23 years old."

print(f"hi {a}, you are {a1} years old")  # Using f-string for formatting


# This code reads the content of a file named "demo.txt" and prints it to the console.

f= open("demo.txt", "r")

content = f.read()
print(content)

# To close the file after reading, we need to call f.close()
# If we don't close the file, it may lead to memory leaks or file corruption.
f.close()

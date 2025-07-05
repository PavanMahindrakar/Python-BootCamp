#if we using f to perform file operations, to close the file we need to write f.close() at the end of the file operations.
# If we don't close the file, it may lead to memory leaks or file corruption.
f= open("demo.txt", "r")
content = f.read()
print(content)
f.close()


#by using with statement, we can automatically close the file after the block of code is executed.
with open("demo.txt", "r") as f:
    content = f.read()
    print(content)

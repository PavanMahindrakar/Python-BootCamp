# write to a file called 'test.txt'
f = open("test.txt", "w")

# write a string to the file
string = "Hello, World!\n"
f.write(string)

f.close()
# append to the file 'test.txt'
f = open("test.txt", "a")
 
# write a string to the file
string = "This is an appended line.\n"
f.write(string)

# close the file
f.close()
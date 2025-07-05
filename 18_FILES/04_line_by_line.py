#read line bye line from a file
# open the file in read mode
f = open("test.txt", "r")
# read the file line by line
for line in f:
    # print each line
    print(line, end='')  # end='' to avoid adding extra newlines    

# close the file
f.close()
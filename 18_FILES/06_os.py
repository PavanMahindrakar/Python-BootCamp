import os
a = os.getcwd()  # Get the current working directory
print(a)
b = os.listdir()  # List all files and directories in the current directory
print(b)
c = os.path.exists('06_os.py')  # Check if a specific file exists
print(c)

d = os.path.join('18_FILES', '06_os.py')  # Join paths
print(d)

# os.remove('sample.txt')  # Remove a file (make sure the file exists)

os.rmdir("dir")  # Remove a directory (make sure the directory is empty)
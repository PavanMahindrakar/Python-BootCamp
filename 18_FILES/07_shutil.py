import shutil

# shutil.rmtree("dir")  # Remove a directory and all its contents
shutil.copy('18_FILES/06_os.py', '18_FILES/copy_of_06_os.py')  # Copy a file

shutil.move('18_FILES/sample.txt', '18_FILES/dir')  # Move a file
s = "\npavan is a grate programmer\n"  #strings are immutable

# name[0] = "R" # This will raise an runtime error because strings are immutable

a=len(s)  # Getting the length of the string
print(a)  # Printing the length of the string

# Converting the string to uppercase
print(s.upper())  # Output: "PAVAN IS A GRATE PROGRAMMER"

# Converting the string to lowercase
print(s.lower())  # Output: "pavan is a grate programmer"

# Converting the first character of each word to uppercase
print(s.title())  # Output: "Pavan Is A Grate Programmer"

# Converting the first character of the string to uppercase
print(s.capitalize())  # Output: "Pavan is a grate programmer"

print(s.strip())  # Removing leading and trailing whitespace (if any)
print(s.lstrip())  # Removing leading whitespace
print(s.rstrip())  # Removing trailing whitespace


print(s.replace("pavan", "Ravan"))  # Replacing "pavan" with "Ravan"
print(s.find("grate"))  # Finding the index of "grate" in the string

# Splitting the string into a list of substrings
text = "Apples, Bananas, Cherries"
print(text.split(", "))  # Output: ['Apples', 'Bananas', 'Cherries']
# Joining a list of strings into a single string
fruits = ['Apples', 'Bananas', 'Cherries']  
print(", ".join(fruits))  # Output: "Apples, Bananas, Cherries"

a = "Pavan0123456789"
print(a.isalnum())  # Checking if the string contains only alphanumeric characters (letters and numbers)
print(a.isalpha())  # Checking if the string contains only alphabetic characters (letters)
print(a.isdigit())  # Checking if the string contains only digits (numbers)
print(a.isspace())  # Checking if the string contains only whitespace characters
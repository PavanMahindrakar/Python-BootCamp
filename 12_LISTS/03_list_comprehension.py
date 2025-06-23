table=[]
for i in range(1,11):
    table.append(5*i)

print(table)  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

# Using list comprehension to create the same table
table_comp = [5*i  for i in range(1, 11)]
print(table_comp)  # Output: [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]

squared_num = [i ** 2 for i in range(5)]
print(squared_num)  # Output: [0, 1, 4, 9, 16]
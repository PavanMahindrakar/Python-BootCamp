table_of_5 = {i: i * 5 for i in range(1, 11)}
print("using comprehensions:", table_of_5)

#this code can be writen in function as follows
def generate_table_of_5():
    return {i: i * 5 for i in range(1, 11)}

generate_table_of_5()
print("using functions:",generate_table_of_5())
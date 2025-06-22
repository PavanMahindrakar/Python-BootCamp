def  add(a, b, plus=0):
    x = a + b + plus
    return x

A1 = add(10, 50, 30) # positional arguments
print(A1)

A2 = add(10, 700) # default value for plus is used 
print(A2)

A3 = add(b=20, a=10, plus=30) #keyword arguments
print(A3)
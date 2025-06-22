#lets write an example for fibonacci series using recursion
'''0 1 1 2 3 5 8 13 21 34 55 89 ...
   0 1 2 3 4 5 6....'''
''' lets itrate this

fib(0)=0
fib(1)=1
fib(2)=fib(1)+fib(0)
fib(3)=fib(2)+fib(1)
fib(4)=fib(3)+fib(2)
fib(5)=fib(4)+fib(3)
fib(6)=fib(5)+fib(4)'''

#function for fib series using recursion
def fib(n):
    if (n == 0 or n == 1): #Base case for fibonacci series
        return n
    return fib(n-2) + fib(n-1) #Recursive case for fibonacci series

print(fib(6))  # Output: 8


#lets Breakdown this program step by step
fib(6)
fib(4) + fib(5)
fib(2) + fib(3) + fib(5)
fib(0) + fib(1) + fib(1) + fib(2) + fib(5)
0 + 1 + 1 + fib(0) + fib(1) + fib(5)
0 + 1 + 1 + 0 + 1 +fib(3) + fib(4)
0 + 1 + 1 + 0 + 1 + fib(2) + fib(1) + fib(4)
0 + 1 + 1 + 0 + 1 + fib(0) + fib(1) + fib(1) + fib(4)
0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(2) + fib(3)
0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + fib(0) + fib(1) + fib(3)
0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 + fib(1) + fib(2)
0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 + 1 + fib(0) + fib(1)
0 + 1 + 1 + 0 + 1 + 0 + 1 + 1 + 0 + 1 + 1 + 0 + 1 = 8
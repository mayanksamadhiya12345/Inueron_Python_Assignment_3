# Write a Python Program to implement your own myreduce() function which works exactly
# like Python's built-in function reduce()

# HERE WE ARE DEFINING OUR OWN myreduce FUNCTION FOR SORTING OUR PROBLEM IN WHICH WE ARE ARE PASS A FUNCTION AND A LIST
def myreduce(func,mylist):
    x = mylist[0]
    for i in range(1,len(mylist)):          # USING FOR LOOP FOR ITERATING THE LIST VALUES
        x = func(x,mylist[i])    
    return x

# ADDTION FUNCTION
def add(a,b):
    return a+b

# MULTIPLICATION FUNCTION
def mul(a,b):
    return (a*b)

# GREATER THAN FUNCTION
def grt(a,b):
    if(a>b):
        return a
    else:
        return b

lst = [2,4,5,10]
print(myreduce(add,lst))
print(myreduce(mul,lst))
print(myreduce(grt,lst))
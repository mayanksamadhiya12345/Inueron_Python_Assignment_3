# Write a Python program to implement your own myfilter() function which works exactly
# like Python's built-in function filter()

# HERE WE ARE DECLARING OUR OWN FILTER FUNCTION  
def myfilter(func,mylist):
    return func(lst)
    

lst = [2,3,4,5,6,7,8,9,0,1,2,3,4,5,7,7]
lst1 = []
lst2 = []

# HERE WE ARE DECLARE A FUNCTION FOR COLLECTING EVEN NUMBERS
def is_even(lst):
    for i in lst:
        if i%2==0:
            lst1.append(i)
    print(lst1)

# HERE WE ARE DECLARE A FUNCTION FOR COLLECTING ODD NUMBERS
def is_odd(lst):
    for i in lst:
        if i%2!=0:
            lst2.append(i)
    print(lst2)

print(myfilter(is_even,lst))
print(myfilter(is_odd,lst))
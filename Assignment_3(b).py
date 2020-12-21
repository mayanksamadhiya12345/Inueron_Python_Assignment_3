# Write List comprehensions to produce the following Lists

# ['A', 'C', 'A', 'D', 'G', 'I', ’L’, ‘ D’]
word = "ACADGILD"
lst1 = [a for a in word]
print(lst1)

# ['x', 'xx', 'xxx', 'xxxx', 'y', 'yy', 'yyy', 'yyyy', 'z', 'zz', 'zzz', 'zzzz']
lst2 = ['x','y','z']
result1 = [i*n for i in lst2 for n in range(1,5)]
print(result1)

# ['x', 'y', 'z', 'xx', 'yy', 'zz', 'xxx', 'yyy', 'zzz', 'xxxx', 'yyyy', 'zzzz']
lst3 = ['x','y','z']
result2 = [i*n for n in range(1,5) for i in lst2]
print(result2)

# [[2], [3], [4], [3], [4], [5], [4], [5], [6]] 
lst4 = [2,3,4]
result3 = [[i+n] for n in range(0,3) for i in lst4]
print(result3)

#[[2, 3, 4, 5], [3, 4, 5, 6],[4, 5, 6, 7], [5, 6, 7, 8]]
lst5 = [2,3,4,5]
result5 = [[i+n for n in range(0,4)] for i in lst5]
print(result5)

# [(1, 1), (2, 1), (3, 1), (1, 2), (2, 2), (3, 2), (1, 3), (2, 3), (3, 3)]
lst6 = [1,2,3]
result6 = [(a,b) for a in lst6 for b in lst6]
print(result6)
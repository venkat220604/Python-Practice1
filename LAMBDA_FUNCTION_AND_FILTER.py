#lambda
square = lambda x:x*x
inp=int(input())
print(square(inp))
#add 
nums=[1,2,3]
squared=list(map(lambda x:x**2,nums))
print(squared)
#filter 
even=list(filter(lambda x: x%2 == 0,nums))
#reduce 
from functools import reduce
total = reduce(lambda x,y : x+y,nums)
print(total)
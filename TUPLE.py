my_tuple=(10,20,30,40,50)
#accessing elements by index
print(my_tuple[0])
print(my_tuple[-1])
#slicing 
print(my_tuple[1:4])
#looping thurough
for item in my_tuple:
    print(item)
#len of tuplex
print(len(my_tuple))    
#check items exits
if 30 in my_tuple:
    print("yes 30 is in tuple")
#tuple concation
tuple1 =(1,2)
tuple2 =(3,4)
result=tuple1+tuple2
print(result)
#tuple repatation
t=(5,6)
print(t*3)
#count and index
sample=(1,1,2,2,3,4,5,5,6,6,6)
print(sample.count(6))
print(sample.index(3))
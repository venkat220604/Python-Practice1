"""print("enter the values into list")
li=[]
for i in range(1,6):
    li1=input(f"enter the values of{i}")
    li.append(li1)
print(li)
"""
#Acess items
thiss_list=["Apple","Banana","Cherry","Kiwi","orange","mango"]
print(thiss_list[1])
#negitive inexing
#negitive indexing means start from end refers-1
print(thiss_list[-1])
#range of indexs
#you can specify the range of index by specifying where to start and where to end the rane
print(thiss_list[2:5])
#pop
thiss_list.pop(1)
print(thiss_list)
#reverse
thiss_list.reverse()
print(thiss_list)
#sort
thiss_list.sort()
print(thiss_list)
#remove
if "Cherry" in thiss_list:
    thiss_list.remove('Cherry')
    print(thiss_list)

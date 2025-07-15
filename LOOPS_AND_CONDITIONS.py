#use fr reverse of a number
num= int(input("Enter the number"))
rev=0
while num>0:
    rev=rev*10+num%10
    num=num//10
print(rev)
#use of for loop
n=[1,2,3]
total=0
for i in n:
    total = total+i
print("Total",total)
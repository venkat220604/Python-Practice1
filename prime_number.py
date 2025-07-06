#prime number 
#take input
n=int(input("enter the value of n"))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count==2:
    print(n,"given number is prime")
else:
    print("not a prime")

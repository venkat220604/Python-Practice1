n=int(input())
sum=0
rem=0
n1=n
while (n!=0):
    rem=n%10
    sum=sum*10+rem
    n=n//10
if n1 == sum:
    print("plaindrome")
else:
    print("not a palindrome")
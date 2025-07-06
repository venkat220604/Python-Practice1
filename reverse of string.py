#n=input()
#print(n[::-1])
s=input()
reversed_str=""
for char in s:
    reversed_str = char + reversed_str
print(reversed_str)
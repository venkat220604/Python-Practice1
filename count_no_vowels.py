n=input()
count=0
for char in n:
    if char == 'a' or char =='e' or char == 'i' or char == 'o' or char == 'u':
        count = count +1
print(count)
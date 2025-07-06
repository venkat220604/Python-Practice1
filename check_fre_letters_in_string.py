text=input("Enter a String")
freq={}
for char in text:
    if char.isalpha():
        char=char.lower()
        if char in freq:
            freq[char]+=1
        else:
            freq[char] =1
print("\n print the frequencies of letters ")
for letter , count in freq.items():
    print(f"{letter}:{count}")
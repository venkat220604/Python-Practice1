#lines read
with open("SAMPLE.txt","r") as file:
    data =file.read()
    print(data)
print("\n \n \n")
#line by line read
with open("SAMPLE.txt","r") as file:
    for line in file:
        print(line.strip())
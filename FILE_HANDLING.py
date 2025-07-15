with open("data.txt","w") as f:
    f.write("Hello hamsini\n")
with open("data.txt","a") as f:
    f.write("Iam Dheeraj")
with open("data.txt","r") as f:
    print(f.read())
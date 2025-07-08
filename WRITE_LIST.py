marks = [85,90,78]
with open("marks.txt","w") as file:
    for mark in marks:
        file.write(str(mark) +"\n")
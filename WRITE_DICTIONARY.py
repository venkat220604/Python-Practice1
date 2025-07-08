student={"name" : "Dheeeraj","age" : 21}
with open("student.txt","w" ) as file:
    for key,value in student.items():
        file.write(f"{key}:{value} \n")
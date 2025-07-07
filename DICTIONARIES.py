student={
    "name" : "dheeraj",
    "age"  : 20,
    "branch" :"ECE",
}
#accessing values 
print(student["name"])
print(student.get("age"))
#Adding/updating values
student["grade"] = "A"
student["age"]="21"
#looping through dictionary
for key,values in student.items():
    print(f"{key}-{values}")
#removing items
student.pop("grade") #also remove grade keys
del student["branch"] #also remove  key
#student.clear() clears entire dictionary
#taking user input using for loop
students={}
for i in range(3):
    name=input(f"Enter name of the student{i+1}")
    marks=int(input(f"enter the marks of {name}"))
    students[name]=marks
print("diictionary ofstudents")
print(students)
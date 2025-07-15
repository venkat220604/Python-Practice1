

class student:
    def __init__(self,name,rollno,marks):
        self.name=name
        self.rollno=rollno
        self.marks=marks
    def to_string(self):
        return f"{self.name},{self.marks},{self.rollno}"
def add_student():
    s=student("Dheeraj",101,[70,80,90])
    with open("student.txt","a") as f:
        f.write(s.to_string())
def show_students():
    with open("student.txt","r") as f:
        print(f.read())
add_student()
show_students()

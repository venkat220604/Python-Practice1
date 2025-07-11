class Person:
    def __init__(self,name):
        self.name=name

class Student(Person):
    def speak(self):
        print(f"{self.name} is studying")
s=Student("Dheeraj")
s.speak()

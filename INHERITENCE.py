class person:
    def __init__(self,name):
        self.name=name
class student(person):
     def speak(self):
         print(f"{self.name} studying")
s=student("Hamsini")
s.speak()

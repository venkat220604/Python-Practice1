class student :
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
    def average(self):
        return sum(self.marks)
    def result(self):
        return "pass" if self.average() >=35 else "fail"
s1=student("Dheeraj",[60,70,80])
print(s1.name,"-",s1.result())
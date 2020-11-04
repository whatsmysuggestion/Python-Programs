
class Student:
    c=0
    def display(self,a,b):
        self.c=a+b
    def displayResult(self):
        print("Sum", self.c)

s=Student()
s.display(10,20)
s.displayResult()
class Person:
    name = ""
    age = 0
    def __init__(self,a,b):
        self.name = a
        self.age = b

    def showName(self):
        print(self.name)

    def showAge(self):
        print(self.age)

person1 = Person("first",100)
person1.showAge()
person1.showName()


person2 = Person("Second",80)
person2.showAge()
person2.showName()

#person1.name="first"
#person1.age=21
#person2 = Person()
#person1.showAge()
#person2.showName()
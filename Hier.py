class Base:
    def geta(self):
        return 10
    def getb(self):
        return 20
class Add(Base):
    def sum(self):
        print(self.geta() + self.getb())

class Minus(Base):
    def sub(self):
        print(self.geta() - self.getb())

f1=Add()
f1.sum()


f2=Minus()
f2.sub()
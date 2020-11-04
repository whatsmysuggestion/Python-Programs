class Base:
    def geta(self):
        return 10
    def getb(self):
        return 20
class Derived1(Base):
    def geta(self):
        return 100
    def sum(self):
        return(super().geta()+self.geta()+self.getb())

d1=Derived1()
print(d1.sum())

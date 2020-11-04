class Base:
    def geta(self):
        return 10
    def getb(self):
        return 20

class Derived1(Base):

    def geta(self,a):
           return a

    def sum(self):
        return(self.getb()+self.geta(10)+self.geta())


d1=Derived1();
print(d1.sum());
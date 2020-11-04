class Base:
    def geta(self):
        return 10
    def getb(self):
        return 20
class Derived1(Base):
    def sum(self):
        return(self.getb()+self.geta())
class Derived2(Base):
    def sub(self):
        return(self.getb()-self.geta())
class LastDerived(Derived1,Derived2):
    def avg(self):
        print(self.sum()+self.sub())
ld=LastDerived()
ld.avg()
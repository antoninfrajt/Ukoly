import math
class Square:
    def __init__(self, a):
        self.a = a
    def obvod(self):
        o = 4*self.a
        return o
    def obsah(self):
        s = self.a*self.a
        return (s)
class Cube(Square):
    def __init__(self, a):
        super().__init__(a)
        self.a = a
    def objem(self):
        print("objem krychle je:" + str(super().obsah()*self.a))
class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def obvod(self):
        o = 2*self.a + 2+self.b
        return o
    def obsah(self):
        s = self.a*self.b
        return (s)
class Kvadr(Rectangle):
    def __init__(self,a,b,c):
        super().__init__(a,b)
        self.c = c
    def objem(self):
        print("objem kvadru je:" + str(super().obsah()*self.c))
class Kruh:
    def __init__(self,r):
        self.r = r
    def obvod(self):
        o = 2*math.pi*self.r
        return o
    def obsah(self):
        s = (self.r^2)*math.pi
        return (s)
class Valec(Kruh):
    def __init__(self,r,v):
        super().__init__(r)
        self.v = v
    def objem(self):
        print("objem valce je:" + str(super().obsah()*self.v))

        
sq = Square(5)
print("obvod čtverce je:"+ str(sq.obvod()))
print("obsah čtverce je:"+ str(sq.obsah()))
c = Cube(5)
c.objem()
rec = Rectangle(5,2)
print("obvod obdelniku je:"+ str(rec.obvod()))
print("obsah obdelniku je:"+ str(rec.obsah()))
kva = Kvadr(5,2,3)
kva.objem()
k = Kruh(6)
print("obvod kruhu je:"+ str(k.obvod()))
print("obsah kruhu je:"+ str(k.obsah()))
val = Valec(6,8)
val.objem()


class A:
    x,y=10,20
    def m1(self):
        print(self.x+self.y)

class B(A):
    a,b=100,200
    def m2(self):
        print(self.a+self.b)

class C(A):
    i,j=1,2
    def m3(self):
        print(self.i+self.j)

c=C()
c.m3() #3
c.m1() #30

b=B()
b.m2() #300
b.m1() #30

a=A()
a.m1() #30
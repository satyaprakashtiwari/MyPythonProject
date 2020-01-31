#invoking parent classs method
class A:
    def m1(self):
        print("this is method from A")

class B(A):
    def m2(self):
        print("this is method from B")
        super().m1() #calling parent class method using super()

b=B()
b.m2()

#invoking parent class variable
class A:
    a,b=10,20

class B(A):
    i,j=100,200
    def m1(self,x,y):
        print(x+y)  #loval variable
        print(self.i+self.j)  #child class variable
        print(self.a+self.b)  #parent class variable

b=B()
b.m1(1,2) # 3
          # 300
          # 30

# when all variable name is same
print("---------------")
a,b=15,20
class A:
    a,b=10,20

class B(A):
    a,b=100,200
    def m1(self,a,b):
        print(a+b)  # local variable
        print(self.a+self.b)  # child class variable
        print(super().a+super().b)  # parent class variable
        print(globals()['a']+globals()['b']) # global variable

obj=B()
obj.m1(1,2) # 3
            # 300
            # 30
            # 35

# invoking constructor
print("######invoking constructor#######")
class A:
    def __init__(self):
        print("constructor from A")

class B(A):
    pass

b=B() # constructor from A---------- if child class has no constructor then super class constructor will be invoked

# when both class have constructor
print("# when both class have constructor")
class A:
    def __init__(self):
        print("constructor from A")

class B(A):
    def __init__(self):
        print("constructor from B")
        super().__init__();  # Approach1: calls parent class constructor
        A.__init__(self)  # Approach2: calls parent class constructor

bobj=B() #constructor from B
         #constructor from A





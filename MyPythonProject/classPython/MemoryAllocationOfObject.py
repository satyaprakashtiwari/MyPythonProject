class MyClass:

    def m1(self):
        pass

c1=MyClass()

c2=MyClass()

c3=c1

#id() displays memory allocation of object
print(id(c1))
print(id(c2))
print(id(c3)) #c1 and c2 will point to same location

print(c1 is c2) #False
print(c1 is c3) #True
print(c1 is not c3) #False
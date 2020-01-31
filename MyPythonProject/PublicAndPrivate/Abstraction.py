#ABC is pre defined abstract class in python

from abc import ABC, abstractmethod
class A(ABC):

    @abstractmethod
    def display(self):
        None

class B(A):

    def display(self):
        print("this is display method")

b=B()
b.display() #this is display method

class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

class Tiger(Animal):

    def eat(self):
        print("eats non veg")

class Cow(Animal):

    def eat(self):
        print("eats veg")

cow=Cow()
cow.eat() #eats veg

tiger=Tiger()
tiger.eat() #eats non veg

#unimplemented method while inheriting from abstract class
class X(ABC):

    @abstractmethod
    def m1(self):
        pass

    @abstractmethod
    def m2(self):
        pass

class Y(X):

    def m1(self):
        print("this is m1")

class Z(Y):

    def m2(self):
        print("this is m2")

"""y=Y() #TypeError: Can't instantiate abstract class Y with abstract methods m2. So we cant instantiate abstarct class
y.m1()"""

z=Z()
z.m1() #this is m1
z.m2() #this is m2



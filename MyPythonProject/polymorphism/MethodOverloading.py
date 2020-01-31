class Human:
    def sayHello(self,name=None):
        if name is not None:
            print("Hello",name)

        else:
            print("Hello")

obj=Human()
obj.sayHello() #Hello
obj.sayHello("Satya") #Hello Satya

#overloading methods
class Bird:
    def fly(self,name=None):
        if name is 'parrot':
            print("can fly")
        if name is 'penguin':
            print("cannot fly")
        else:
            print("no input")

obj1=Bird()
obj1.fly('parrot') #can fly
obj1.fly('penguin') #cannot fly
obj1.fly() #no input



#overriding a variable
class Parent:
    name="satya"

class Child(Parent):
    name="tiwari"

obj=Child()
print(obj.name) #tiwari

#overriding a method
class Bank:
    def rateOfInterest(self):
        return 0

class ICICI(Bank):
    def rateOfInterest(self):
        return 10.5;

obj=ICICI()
print(obj.rateOfInterest()) #10.5

c=Bank()
print(c.rateOfInterest()) #0

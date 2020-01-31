# approach 1
import Operation

Operation.add(10,20) #30
Operation.mul(10,30) #300

# approach 2
from Operation import add,mul

add(10,30) #40
mul(10,40) #400

# approach 3
from Operation import *

add(10,30) #40
mul(10,40) #400

print("-----------########------------")
#appraoch 1
import Animal
import Bird

Animal.fly() #animal cant fly
Animal.color()  #animal is black

Bird.fly() #bird cant fly
Bird.color() #bird is green

#approach 2
from Animal import *

fly() #animal cant fly
color() #animal is black

from Bird import *

fly() #bird cant fly
color() #bird is green

#approach1
import A
import B

obj=A.Animal()
obj.display() #i like cow

obj2=B.Bird()
obj2.display() #I like parrot

#approach 2
from A import Animal
from B import Bird

obj3=Animal()
obj3.display() #i like cow

obj4=Bird()
obj4.display() #I like parrot

#get all classes and function in module
import M

print(dir(M)) #['A', 'B', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', 'm3', 'm4']

#this will not list methods
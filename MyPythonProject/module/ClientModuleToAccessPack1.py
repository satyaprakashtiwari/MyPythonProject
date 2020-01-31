import sys

sys.path.append("C:/Users/satyatiw/PycharmProjects/PythonLearning/pack1")

#approach1
import Module1
import Module2

Module1.display() #this is display method from module1
Module2.show() #this is show method from module2

#approach2
from Module1 import *
from Module2 import *

display() #this is display method from module1
show() #this is show method from module2
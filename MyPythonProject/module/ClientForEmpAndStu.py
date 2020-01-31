import sys

sys.path.append("C:/Users/satyatiw/PycharmProjects/PythonLearning/pack1")
from Emp import Employee

e=Employee(101,"Satya",79889)
e.dispemp() #EMPID:101  EMPNAME:Satya  ESAL:  79889

sys.path.append("C:/Users/satyatiw/PycharmProjects/PythonLearning/pack3")
from Stu import Student

s=Student(102,"Ankit","A")
s.display() #Sid: 102 Sname: Ankit Sgrad: A


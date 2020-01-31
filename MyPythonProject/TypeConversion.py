'''num1= input("enter first decimal number: ")   # 10.5 user first input
num2= input("enter second decimal number: ")  #10.5 user second input
print(float(num1)+float(num2)) # 21.00 is output '''



''' num3= input("enter first decimal number: ")   # 10.5 user first input
num4= input("enter second decimal number: ")  #10.5 user second input
print(float(num3)+int(num4)) # ValueError: invalid literal for int() with base 10: '10.5' '''

''' num5= input("enter first decimal number: ")   # 10.5 user first input
num6= input("enter second integer number: ")  #10 user second input
print(float(num5)+int(num6)) #20.5         float can hold int but int can't hold float '''

num1= input("enter first decimal number: ")   # 10.5 user first input
num2= input("enter second decimal number: ")  #10 user second input
print(float(num1)+float(num2))  # 20.5 float can hold int but int can't hold float


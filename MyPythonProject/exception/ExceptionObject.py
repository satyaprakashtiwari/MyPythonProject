try:
    number=one
    print("the number is ",number)

except NameError as e:
    print("Exception is: ",e)

finally:
    print("welcome to finally")
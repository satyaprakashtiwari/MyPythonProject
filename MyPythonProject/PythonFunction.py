def myFunction():
    pass

myFunction()

def sum(start,end):
    result=0
    for i in range(start, end+1):
        result=result+i
    print(result)


sum(10,20) #165 is the sum from numbers between 10 and 20

def sum1(start,end):
    result=0
    for i in range(start, end+1):
        result=result+i
    return result

s=sum1(10,20)
print(s) #165

def sum2(start,end):
    if start>end:
        print("start value must be less than end value")
        return
    result = 0
    for i in range(start, end + 1):
        result = result + i
    return result

s=sum2(20,10)
print(s) #start value must be less than end value
          #None

def test():
    i=90

print(test()) #None because there is no return. if you are using return, then it must return something


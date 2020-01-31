def enterage(age):
    if age < 0:
        raise ValueError("only positive value are allowed")

    if(age % 2==0):
        print("age is even")
    else:
        print("age is odd")

try:
    num = -1
    enterage(num)
except ValueError:
    print("only positive value allowed")

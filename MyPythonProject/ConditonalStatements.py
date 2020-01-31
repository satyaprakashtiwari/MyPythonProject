a=30
if a>20:           # 0 represent false -----------1 represent true
    print("a is greater than 20")
    print("a is greater than 20")
else:
    print("a is less than 20")
    print("a is less than 20")


num=15
if num%2==0:
    print("number is even")
else:
    print("number is odd")

# single statement in single single line
print("welcome") if False else print("India")
print("welcome") if 10<20 else print("India")

# multiple statement in single line
{print("welcome1"),print("welcome2")} if True else {print("India1"),print("India2")}

# elif conditon
a=30
if a==10:
    print("a==10")
elif a==20:
    print("a==20")
elif a==30:
    print("a==30")
else:    # else is optional when used with elif
    print("Number is out of scope")


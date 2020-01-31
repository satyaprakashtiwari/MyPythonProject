global_var=12  #global variable

def fun():
    local_var=100;
    print(global_var)

fun() #12

#print(local_var) #ameError: name 'local_var' is not defined

xy=100

def cool():
    xy=200
    print(xy)

cool() #200 local variable has high priority than global varaible
print(xy) #100


t=1

def increment():
    #global t=10 #SyntaxError: invalid syntax.   Declaration in one line and initialisation in another line
    global t
    t=5
    print(t)

increment() #5
print(t) #5

#passing arguments with default values (position)

def funct(i,j=50):
    print(i,j)

funct(1000) #1000 50
funct(67,90) #67 90

#positional arguments
def named_args(name, greetings):
    print(greetings," ",name)

named_args("satya", "welcome")  #welcome   satya  POSITIONAL ARGUMENTS

named_args(name='ankit',greetings='good morning') #good morning   ankit  KEYWORD ARGUMENTS order is not important
named_args(greetings='good morning',name='ankit') #good morning   ankit  KEYWORD ARGUMENTS

#mixing of keyword and position
def my_func(a,b,c):
    print(a,b,c)

my_func(10,20,30) #10 20 30  positional
my_func(10, b=20, c=30) #10 20 30  positional, keyword, keyword
my_func(10, c=30, b=20) #10 20 30

#starts with postion then keyword argument
#my_func(b=20, c=30, 10)

#multiple returns then it will return tuple
def bigger(a,b):
    if(a>b):
        return a,b
    else:
        return b,a

s=bigger(100,200)

print(s) #(200, 100)
print(type(s)) #<class 'tuple'>
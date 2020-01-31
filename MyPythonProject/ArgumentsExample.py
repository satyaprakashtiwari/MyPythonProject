def sum(*args):  # we can use *a, *b etc
    s=0
    for i in args:
        s=s+i

    print(s)

sum(10,20) #30
sum(1,5,9) #15
#------------------
def display(a,b,c):
    print(a,b,c)

args=[1,2,3] # argument must be asame as number of parameter
display(*args) #1 2 3

print("--------------")

def my_three(a,b,c):
    print(a,b,c)

x={ 'a' :1 , 'b' : 5 , 'c' :8}

my_three(**x) #1 5 8

def my_funct(**kargs):
    for i,j in kargs.items():
        print(i,j)

my_funct(name="tom", spot="football", roll=90) #name tom
                                               #spot football
                                                #roll 90

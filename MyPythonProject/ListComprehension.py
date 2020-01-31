
for x in range(10):
    print(x)

list1=[x for x in range(10)]
print(list1) #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

list2=[x+1 for x in range(10)]
print(list2) #[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# to print even number
for x in range(10):
    if(x%2==0):
        print(x)

list3=[x for x in range(10) if(x%2==0)]  #for storing even number in list
print(list3)  #[0, 2, 4, 6, 8]
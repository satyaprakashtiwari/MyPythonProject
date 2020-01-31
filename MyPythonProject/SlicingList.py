list=[78,12,35,77,85,45]

print(list[0:5]) #[78, 12, 35, 77, 85]

print(list[:3]) #[78, 12, 35]

print(list[2:]) #[35, 77, 85, 45]

#+ and * operator
l1=[34,78]
l2=[77,12,90]
l3=l1+l2;
print(l3) #[34, 78, 77, 12, 90]

l4=l1*5
print(l4) #[34, 78, 34, 78, 34, 78, 34, 78, 34, 78]

print(77 in l2) #True
print(78 not in l2) #True

#list traversing
list=[45,66,35,34,2]

for i in list:
    print(i, end=" ")  # printing in same line

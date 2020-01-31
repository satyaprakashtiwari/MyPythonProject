#creating list

list1=list();
print(list1) #[] epmty list is created

list2=list([23,54,12])
print(list2)  #[23, 54, 12]

list3=list(["Satya",54,"Tiwari"])
print(list3) #['Satya', 54, 'Tiwari']


list4=list("python")
print(list4)  # ['p', 'y', 't', 'h', 'o', 'n']

# accessing element form list
l=[1,3,65,2]
print(l[2]) #65 as it is present at 2nd position
print(l[0])  #1

list=[6,2,4,24,5]

print(2 in list) #True
print(90 not in list) #True
print(len(list)) #5 is size of list
print(max(list)) #24 is highest number in list
print(min(list)) #2 is lowest number in list
print(sum(list)) #41 is sum of all values in list
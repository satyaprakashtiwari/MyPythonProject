list1=[2,3,4,1,32,4]

list1.append(19)  # add item to end of list
print(list1) #[2, 3, 4, 1, 32, 4, 19]

print(list1.count(4))  #2 ---------- 4 is repeated 2 times

list2=[99,54]

list1.extend(list2)
print(list1) #[2, 3, 4, 1, 32, 4, 19, 99, 54]

print(list1.index(4)) # returns index of 2
print(list1.index(32)) # returns index of 4

list1.insert(1,25) # 25 to 1st position
print(list1) #[2, 25, 3, 4, 1, 32, 4, 19, 99, 54]

# removing a value from list
print(list1.pop(2)) # 3   ----returns and remove element at 2nd position
print(list1) #[2, 25, 4, 1, 32, 4, 19, 99, 54]

print(list1.remove(32)) #returns null and remove an item 32 from list
print(list1) #[2, 25, 4, 1, 4, 19, 99, 54]

#reversing the list
list1.reverse(); #[54, 99, 19, 4, 1, 4, 25, 2]
print(list1)

#sort list
list1.sort()
print(list1) #[1, 2, 4, 4, 19, 25, 54, 99]



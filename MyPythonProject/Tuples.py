t1=()

t2=(12,345,76)

print(t1) #()
print(t2) #(12, 345, 76)

t3=([667,64,24])
print(t3) #[667, 64, 24]

t4=tuple("abc")
print(t4) #('a', 'b', 'c')

t5=(23,53,99,29,12)

print(max(t5)) #99 is max
print(min(t5)) #12 is min
print(len(t5)) #5 is lenght
print(sum(t5)) #216 is sum of items

#iteration

for x in t5:
    print(x, end=" ") #23 53 99 29 12

#slicing
print(t5[:4]) #(23, 53, 99, 29)
print(t5[0:3]) #(23, 53, 99)
print(t5[0:]) #(23, 53, 99, 29, 12)

print(23 in t5) #True
print(1 in t5) #False
print(1 not in t5) #True
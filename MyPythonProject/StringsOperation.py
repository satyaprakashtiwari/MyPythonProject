#creating strings

# approach 1
name="john"
name='john'
print(name)

# approach 2
name1= str("abc")
print(name1)
print(type(name1))

# string is immutable
str1="abc"
str2="abc"
print(id(str1),id(str2))

# use of + for concatinaiton    and * for printing multiple times
str="satya"
print(str+" welcome to python")

print(str*5)
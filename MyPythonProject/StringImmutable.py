str1="welcome"
str2="welcome"

print(id(str1),id(str2)) # both are at same location

str2=str2+"abc"
print(id(str1),id(str2))

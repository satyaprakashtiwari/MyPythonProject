s="Python"

for i in s:
    print(i)


s="welcome to python"

print(s.isalnum())  #false
print("welcome".isalpha())   #true
print("2020".isdigit())  #true
print("first number".isidentifier()) #false
print(s.islower()) #true
print("WELCOME".isupper()) #true
print(" ".isspace()) #true
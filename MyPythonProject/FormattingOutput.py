name="John"
age=25
sal=10000.25

# approach 1
print(name, age, sal)

# approach 2
print("Name is ", name)
print("Age is ", age)
print("Salary is ", sal)

# approach 3  using % operator. Type of data is important
print("Name:%s Age:%d Salary:%g"%(name, age, sal))

# approach 4 using {}. value is important
print("Name:{} Age:{} Salary:{}".format(name,age,sal))

# approach 5 using {} with index. Index starts with 0
print("Name:{0} Age:{1} Salary:{1}".format(name,age,sal))
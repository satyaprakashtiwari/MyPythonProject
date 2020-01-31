s="welcome to python"

print(s.endswith("on"))  #true
print(s.startswith("good")) #false
print(s.find("come")) # 3 as it is present at 3
print(s.find("become")) #-1 as substring is not present
print(s.rfind("o")) #15 as o is lastly present at 15th position
print(s.count("o"))  # o has occurred 3 times
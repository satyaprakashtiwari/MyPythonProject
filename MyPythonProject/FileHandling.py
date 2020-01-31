#writing to file
file=open("myDataFile","w")

file.write("Satya, how are you?\n")
file.write("Satya, proud of you\n")

file.close()

#reading data from file all at once
file=open("myDataFile","r")
#print(file.read()) #read entire file at once

#print(file.read(10)) #read first 10 characters

#print(file.readlines()) #['Satya, how are you?\n', 'Satya, proud of you\n'] read entire file at once in array format

print(file.readline()) #reads only first line
file.close()

#appeding the file
file=open("myDataFile","a")
file.write("This is last line of a file")
file.close()

#reading data from loop
file=open("myDataFile","r")
for f in file:
    print(f)
file.close()





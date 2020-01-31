print("prog started")
#print(10/0) #ZeroDivisionError: division by zero
try:
    print(10/5) #2.0
    #print((10/0)) #entered except block

except ZeroDivisionError:
    print("entered except block") #if ZeroDivisionError is thrown then only this block will execute
except TypeError:
    print("there was type mistake")
else:
    print("entered into else block when exception dont occur")
#case 1--- exception occured ---->except then finally
#case 2--- exception not thrown----> else then finally
#case 3---exception occured when not handled------ finally
finally:
    print("this block will always execute, if exception occurs or not")

print("prog ended")
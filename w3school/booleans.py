
#--------------------- Booleans

print(2>5)
print(32<102)
print(4==4,"\n")


a=100
b=22
if b>a:
    print("b is greater\n")
else:
    print("a is greater\n")


#True
print(bool("Hello"))
print(bool(20))
print(bool(["red","blue","yellow"]),"\n")

def myfunc():
    return True
print(myfunc())

#False
print("\n")
print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool({}))
print(bool({}),"\n")

class myclass():
    def __len__(self):
        return 0
myobj=myclass()
print(bool(myobj),"\n")


#----
def myFunction():
    return True
    #return False #output "No"
if myFunction():
    print("Yes","\n")
else:
    print("No","\n")


x=100
print(isinstance(x,int))




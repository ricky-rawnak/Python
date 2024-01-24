
''' 
    List is a collection which is ordered and changeable. Allows duplicate members.
    Tuple is a collection which is ordered and unchangeable. Allows duplicate members.
    Set is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
    Dictionary is a collection which is ordered** and changeable. No duplicate members.
'''

'''
Text Type: 	str

Numeric Types: 	int, float, complex

Sequence Types: 	list, tuple, range

Mapping Type: 	dict

Set Types: 	set, frozenset

Boolean Type: 	bool

Binary Types: 	bytes, bytearray, memoryview

None Type: 	NoneType
'''


#--------------------- Data Types

# []        --> list
# ()        --> tuple
# {}        --> set 
# ({})      --> frozenset 
# {"":""}   --> dict

'''

a=complex(9)
a1=9j
a2=8.0
a3="Ok"
a4=["n","i","c","e"]
a5=("n","i","c","e")
a6={"n","i","c","e"}
a7=range(6)
a8={"1st work":"good","2nd word":"student"}
a9=frozenset({"n","i","c","e"}) #its elements cannot be modified after creation.
a10=True
a11=b"This is a bytes" #immutable
a12=bytearray(5) #can be modified after creation
a13=memoryview(bytes(5)) #efficiently manipulate binary data
a14=None #constant

print(f"{a} is: ",a)
print(f"{a1} Type is: ",type(a1),"\n")
print(f"{a2} Type is: ",type(a2),"\n")
print(f"{a3} Type is: ",type(a3),"\n")
print(f"{a4} Type is: ",type(a4),"\n")
print(f"{a5} Type is: ",type(a5),"\n")
print(f"{a6} Type is: ",type(a6),"\n")
print(f"{a7} is: ",a7)
print(f"{a7} Type is: ",type(a7),"\n")
print(f"{a8} Type is: ",type(a8),"\n")
print(f"{a9} is: ",a9)
print(f"{a9} Type is: ",type(a9),"\n")
print(f"{a10} is: ",a10)
print(f"{a10} Type is: ",type(a10),"\n")
print(f"{a11} is: ",a11)
print(f"{a11} Type is: ",type(a11),"\n")
print(f"{a12} is: ",a12)
print(f"{a12} Type is: ",type(a12),"\n")
print(f"{a13} is: ",a13)
print(f"{a13} Type is: ",type(a13),"\n")
print(f"{a14} is: ",a14)
print(f"{a14} Type is: ",type(a14),"\n")


'''
#--------------------- Numbers

'''

b=8
b1=249489124982193892
b2=-5
b3=1.10
b4=4.0
b5=-3.1416
b6=45e45 #45E45
b7=-212.8e2
b8=-4.4E2
b9=3+5j
b10=2j
b11=-10j

x=float(b)
x1=int(b3)
x2=complex(b)

print(f"{b} Type is: ",type(b),"\n")
print(f"{b1} Type is: ",type(b1),"\n")
print(f"{b2} Type is: ",type(b2),"\n")
print(f"{b3} Type is: ",type(b3),"\n")
print(f"{b4} Type is: ",type(b4),"\n")
print(f"{b5} Type is: ",type(b5),"\n")
print(f"{b6} Type is: ",type(b6),"\n")
print(f"{b7} Type is: ",type(b7),"\n")
print(f"{b8} Type is: ",type(b8),"\n")
print(f"{b9} Type is: ",type(b9),"\n")
print(f"{b10} Type is: ",type(b10),"\n")
print(f"{b11} Type is: ",type(b11),"\n")

# Type convert

print(f"{x} Type is: ",type(x),"\n")
print(f"{x1} Type is: ",type(x1),"\n")
print(f"{x2} Type is: ",type(x2),"\n")


# Random number

import random
print(random.randrange(1,5))


'''

#--------------------- Casting

c=int(6)
c1=int(3.8416)
c2="7"

#integer
print(c)
print(c1)
print(c2)

#float
print(float(9))
print(float(5.1))
print(float("7.22"))
print(float("53"))

#strings
print(str("hi"))
print(str(20))
print(str(31.4))



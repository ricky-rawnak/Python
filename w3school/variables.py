
#========== Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

#     A variable name must start with a letter or the underscore character
#     A variable name cannot start with a number
#     A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
#     Variable names are case-sensitive (age, Age and AGE are three different variables)
#     A variable name cannot be any of the Python keywords.


#========== Illegal variable names:
# 2myvar = "John"
# my-var = "John"
# my var = "John" 

'''
#--------------------- variable names

a=5
a=7
A=9
b=float(9)
_carname="BMW"
color='red'
thisIsCamelCase="Camel"
ThisIsPascalCase="Pascal"
this_is_snake_case="Snake"

print(a)
print(type(a))
print(A)
print(b)
print(_carname)
print(color)
print(thisIsCamelCase)
print(ThisIsPascalCase)
print(this_is_snake_case)


#--------------------- multiple values

x,y,z="orange","kiwi","mango"
print(x)
print(y)
print(z)

x1=y1=z1="book"
print(x1)
print(y1)
print(z1)

fruits=["banana","apple","cherry"]
x2,y2,z2=fruits
print(x2)
print(y2)
print(z2)

#--------------------- output variables

m="python"
n="is"
o="awesome"

m1="python "
n1="is "
o1="awesome "

m2=98
n2=2
o2="Sally"

print(m,n,o) #comma creates auto spacing
print(m1+n1+o1) #needs spacing
print(m2+n2)
#print(m2+o2) #will throw error
print(m2,o2)


'''
#--------------------- Global variables

j="awesome"     #global as its created outside function
def myfunc():
    print("Python is "+j)
myfunc()


k="checking"      #global as its created outside function
def myfunc1():
    k="verified"  #local variable
    print("Local variable "+k)
myfunc1()
print("Local variable "+k)



def myfunc2():
    global l
    l="tough"
myfunc2()
print("Local variable "+l)


q="fantastic"
def myfunc3():
    global q
    q="not easy"
myfunc2()
print("Local variable "+q)


































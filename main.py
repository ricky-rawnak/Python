'''
-- link : https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg
--Multiple line comment
--Author: Ricky
--Goal: Learn Python
--Everything in python is object:int,float,string,list,map etc"
--alt+shift+down_arrow=copy lines
--[0:4] #including 0 but not 4
--strings are immutable
'''
'''
#1------------------------------ print
print("hello world")
print(3+6)
print(8-9)

#2------------------------------ new line
print("Python is one of the most demanded programming languages in the job market.\nSurprisingly, it is equally easy to learn and master  Python.")
print("hey",1,2,3,sep="...",end="009\n")
print("Ricky")

#3------------------------------ variable
a=121938918319
print(a)
car=9
b=car
print(b)
c="Truck"
print(c)

#4------------------------------ Type
a1=2
a2=5
b1="Boat"
c1=2.3
d1=False
print(a1+a2)
print("The type of a is: ",type(a1))
print("The type of b is: ",type(b1))
print("The type of c is: ",type(c1))
print("The type of d is: ",type(d1))

#5------------------------------ list,tuple,map
list1=[2,5,1,[-3,2],["red","blue"]]
print(list1)
tuple1=(("cow","cat"),("tiger","lion"))
print(tuple1)
dict1={"name":"Edward","age":20,"canVote":True}
print(dict1)

#6------------------------------ operators
print(10+6)
print(10-6)
print(10*6)
print(10/6)
print(10//6) # no divider
print(10%6) #remainder  > 6/10/1 remainder 10-6=4
print(4**3)

#7------------------------------ typecasting
a3="5"
a4="122"
print(int(a3)+int(a4))

c3=1.22
c4=8
print(c3+c4)

#8------------------------------ input function
a5=input("Enter your name: ")
print("My name is",a5)
x=input("Enter value of x: ")
y=input("Enter value of y: ")
print(x+y)
print(int(x)+int(y))

#9------------------------------ strings
name="Tom"
friend="Jerry"
anotherFriend='Josh'
convo='''
# Jerry said, Hurry up, come fast,
"I want cheese"'''
print("Hello,"+name)
print(name[0])
print(name[1])
print(name[2])
#print(convo)
print("Let's use for-loop:\n")
for character in convo:
    print(character)

#10------------------------------ string slicing
#
colors="Blue,Red,yellow"
print(colors[0:6])
print(len(colors))
#
fruits="Strawberry"
len1=len(fruits)
print("Strawberry is a",len1,"letter word")
print(fruits[0:-4]) #len(fruits)=10, 10-4=6, strawb(6)
print(fruits[-4:-1]) #len(fruits)=10, (10-4=6,10-1=9,),6:9 err(3), 6th to 8th index
#
nm="Harry"
print(nm[-4:-2]) #len(nm)=5, 1:3, ar(2), 1st to 2nd index

#11------------------------------ string methods
#
str="Carry!! !!!!!!! Carry"
print(len(str))
print(str.upper())
print(str.lower())
print(str.rstrip("!"))
print(str.replace("Carry", "Above"))
print(str.split(" "))
print(str.count("Carry"))
#
blogHeading="introduction to pyThon"
print(blogHeading.capitalize())
#
str1="Welcome to the 100 days python tutorial!!!"
print(len(str1))
print(str1.center(50))
print(str1.endswith("!!!"))
print(str1.endswith("to",4,10))
print(str1.find("the"))
print(str1.istitle())
print(str1.startswith("Welcome"))
print(str1.title())
#
str2="WelcomeToParis"
print(str2.isalnum())
print(str2.isprintable())
print(str2.swapcase())
#
str3="Welcome00"
print(str3.isalpha())
#
str4="      "
print(str4.isspace())

#12------------------------------ if-else/nested
#
a =int(input("Enter age: "))
print("Age is : ",a)
print(a>18)
print(a<=18)
print(a==18)
print(a!=18)
if(a>18):
    print("Allowed to drive")
else:
    print("Not allowed to drive")

#
applePrice=125
budget=190
if(applePrice<=budget):
    print("Add 1kg apple")
else:
    print("Do not add")
#
num=int(input("Enter number: "))
if(num<0):
    print("Negative")
elif(num==0):
    print("Zero")
elif(num==999):
    print("Special")
else:
    print("Positive")
print("Happy Now!!!")

#------------------------------ nested
n=int(input("Enter N: "))
if(n<0):
    print("Negative")
elif(n>0):
    if(n<=10):
        print("Between 1-10")
    elif(n>10 and n<=20):
        print("Between 11-20")
    else:
        print("Greater than 20")
else:
    print("Zero")

#------------------------------ Match Case Statements
x=int(input("Enter value of x: "))
match x:
    case 0:
        print("x zero")
    case 4  if x%2==0:
        print("x%2==0 and case is 4")
    case _ if x<10:
        print("x <10")
    case _ if x!=90:
        print(x,"is not 90")
    case _ if x!=80:
        print(x,"is not 80")
    case _:
        print(x)

#------------------------------ For loop

cars='lumberjack'
for i in cars:
    #print(i)
    print(i,end=", ")

colors=["Red","Green","Blue","Yellow"]
for color in colors:
    print(color)
    for i in color:
        print(i)

# for k in range(10):
for k in range(1,200):
    print(k)

for j in range(1,12,3):  #range 1-11 ,3-> 3 step
    print(j)  #1, 1+3=4, 4+3=7, 7+3=10

#------------------------------ while loop

k=int(input("Enter start value of k: "))
while(k<=26):
    k=int(input("Enter the number: "))
    print(k)
print("Loop ended")

count =5
while(count>0):
    print(count)
    count=count-1
else:
    print("I am inside else")

#------------------------------ break and continue
for i in range(12):
    if(i==10):
        continue
    print("5 X",i+1,"=",5*(i+1))
print("Break is Stop the loop ,continue is skip the iteration")

i=0
while True:
    print(i)
    i=i+1
    if(i%100==0):
        break

#------------------------------ functions

def caclGmean(a,b):
    gmean=(a*b)/(a+b)
    print(gmean)

def isGreater(a,b):
    if(a>b):
     print("First number is greater")
    else:
     print("Second number is greater")

def isLesser(a,b):
   pass
a=2
b=8
c=8
d=7
isGreater(a,b)
caclGmean(a,b)
isGreater(c,d)
caclGmean(c,d)
# gmean1=(a*b)/(a+b)
# print(gmean1)
# gmean2=(c*d)/(c+d)
# print(gmean2)

#------------------------------ functions arguments

def average(a=9,b=1):
    print("The average is : ",(a+b)/2)
average(1,5)

def name(fname,mname="Crystal",lname="Windsor"):
    print("Hello, ",fname,mname,lname)
name("Emiliey")

def average(*numbers):
    sum=0
    for i in numbers:
        sum=sum+i
    # print("Average is: ",sum/len(numbers))
    return sum/len(numbers)
c=average(5,6,1,8,2)
print(c)

def name(**name):
    print("Hello,",name["fname"],name["mname"],name["lname"])
name(mname="Leo",lname="Messi",fname="Jr")

#------------------------------ List

l=[2,5,6,"python",True]
print(l)
print(type(l))
print(l[-3]) #neg index
print(l[len(l)-3]) #total length 5
print(l[2]) # 0 1 2 => index 2 =6

if 5 in l:
    print("yes")
else:
    print("No")

if "on" in "python":
    print("yes it does")

marks=[62,55,70,"subject",True,39,83,91,61,10,29]
print(marks[:]) # all 0:len(marks)
print(marks[1:]) # index starts from 1 to end
print(marks[1:-1]) # -1=>len(marks)-1=>11-1=>10 # index 1 to 10
print(marks[1:8]) 
print(marks[1:8:2]) # first do 1:8 then take the value to skip of "2"

lst=[i for i in range(4)]
print(lst)
lst1=[i*i for i in range(10)]
print(lst1)
lst2=[i*i for i in range(10) if i%2==0]
print(lst2)

#------------------------------ List methods

l=[11,45,1,2,4,6,1,2]
print(l)
# l.append(7) # add 7 in list
# l.sort() #big to small
# l.sort(reverse=True) # small to big
# print(l.index(2)) #value 2 is in index 3
# print(l.count(1)) #how many 1 
# m=l.copy()
# m[0]=0
#l.insert(1,999)  # insert 999 in index 1
m=[900,1000,1100]
k=l+m
print(k)
l.extend(m) #add the values of m at the end of l
print(l)

#------------------------------ Tuples

tup={1,5,6}
tup1=(1,5,49,31,"red")
tup2={1,}
print(type(tup),tup)
print(type(tup1),tup1)
print(type(tup2),tup2)
print(tup1[0])
print(tup1[1])
print(tup1[2])

if 31 in tup1:
    print("yes 31 exists")
tupNew=tup1[1:4]
print(tupNew)


#------------------------------ Operations on Tuples

fruits=("mango","apple","strawberry","papaya","kiwi")
temp=list(fruits)
temp.append("guava") #add item
temp.pop(3)          #remove
temp[2]="jackfruit"  #change 
fruits=tuple(temp)
print(fruits)

countries=("bangladesh","australia","china","iran")
countries2=("russia","nigeria","palestine")
world=countries+countries2
print(world)

tuple1=(0,1,2,3,2,3,4,3,2)
# res = tuple1.count(3)
# res = tuple1.index(4)
# res = tuple1.index(3,4,8)
res = len(tuple1)
print(res)


#------------------------------ f-strings

letter="Hey my name is {1} I am from {0}"
country="Bangladesh"
name="Ricky"
#print(letter.format(name,country))
print(letter.format(country,name))

print(f"Hey my name is {name} I am from {country}")
print(f"Hey my name is {{name}} I am from {{country}}")


txt="For only {price:.2f} dollars"
print(txt.format(price=23.0555))

print(f"{20*5}")
print(type(f"{3*8}"))

'''

#------------------------------ Docstrings

# def square(n):
#     '''Takes in a number n,
# returns the square n'''
#     print(n**2)
# square(5)
# print(square.__doc__)

#PEP 8

#cmd run => python , import this

'''
#------------------------------ Recursion

#factorial(7): 7*6*5*4*3*2*1
#factorial(6): 6*5*4*3*2*1
#factorial(5): 5*4*3*2*1
#factorial(4): 4*3*2*1
#factorial(0): 1

#factorial(n): n*factorial(n-1)

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return  n*factorial(n-1)

print(factorial(3))
print(factorial(4))
print(factorial(5))

#fibonacci
#f0=0
#f1=1
#f2=f1+f0
#f(n)=f(n-1)+f(n-2)

def fibonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

print(fibonacci(3))
print(fibonacci(7))
print(fibonacci(1))
print(fibonacci(0))

#------------------------------ set

s={2,4,2,5,6,5}
print(s)

info={"carla",11,False,7.9,11,2}
print(info)

g=set()
print(type(g))

for value in info:
    print(value)

#------------------------------ set methods

#union
s1={1,2,5,6}
s2={3,6,7}
print(s1.union(s2))
s1.update(s1)
print(s1,s2)

cities={"Tokyo","Madrid","Seol","Berlin"}
cities2={"Tokyo","Baghdad","Delhi","Madrid"}
cities3=cities.union(cities2)
print(cities3)

#intersection
cities4=cities.intersection(cities2)
print(cities4)

#symmetric difference => not common
cities5=cities.symmetric_difference(cities2)
print(cities5)

#difference => A-B
cities6=cities.difference(cities2)
print(cities6)

#isdisjoin=>no intersection
cities7=cities.isdisjoint(cities2)
print(cities7)

#issuperset B needs to be in A
cities8=cities.issuperset(cities2)
print(cities8)

#issubset 
cities9=cities.issubset(cities2)
print(cities9)

#add
cities.add("Dhaka")
print(cities)
cities.remove("Tokyo")
print(cities)
cities.discard("Madrid2")
print(cities)

#pop => removes last item
item=cities.pop()
print(item)

#del => removes whole set
#del cities
print(cities)

#clear
cities.clear()
print(cities)

#check
element={"O2","CO2","H2SOW"}
if "O2" in element:
    print("Present")
else:
    print("Absent")


#------------------------------ Dictionaries

dic={
    "Ricky": "Human being",
    "Spoon": "Object"
}
print(dic["Ricky"])

dic={
    344:"Alex",
    29:"James",
    577:"Kiana",
    401:"Edward"
}
print(dic[577])

info={'name':'Jack','age':27,'eligible':True}
print(info)
print(info['name'])
print(info.get('eligible'))
print(info.keys())
print(info.values())

#to throw error =>
#print(info['name2'])
#print(info.get('name2'))

for key in info.keys():
    print(f"The value of key {key} is :{info[key]}\n")
    #print(info[key])

print(info.items())
for key, value in info.items():
    print(f"\nThe value of key {key} is :{value}")


#------------------------------ Dictionaries methods

ep1={122:45,128:76,324:11,954:89}
ep2={31:97,427:95}
#ep1.update(ep2)
#ep1.clear()
#del ep1
#ep1.pop(122) #removes 1st
#ep2.popitem() #removes last
del ep1[122]
print(ep1)
print(ep2)


#------------------------------ for Loop with else

for i in range(5):
#for i in []:
    print(i)
    if i==4:
        break
else:
    print("sorry no i\n\n")



j=0
while j<7:
    print(j)
    j=j+1
    # if j==4:
    #     break
else:
    print("sorry no j")

#------------------------------ Exception Handling

a=input("enter number: ")
print(f"multiplication table of {a} is: ")
try:
    for i in range(1,11):
        print(f"{int(a)}x {i} ={int(a)*i}")
except Exception as e:
    print("sorry some problem occured. invalid input")
print("some imp lines of code")
print("end of program")


try:
    num=int(input("enter num: "))
    a=[6,3]
    print(a[num])
except ValueError:
    print("number is not an integer")
except IndexError:
    print("Index error")



#------------------------------ keyword

def func1():
 try:
    l=[1,5,6,7]
    i=int(input("enter index: "))
    print(l[i])
    return 1
 except:
    print("Some error occured")
    return 0
# finally:
#     print("I am always executed")
print("I am always executed")
x=func1()
print(x)


#------------------------------ custom error


a=int(input("enter value between 5 and 9: "))
if(a<5 or a>9):
    raise ValueError("value should be between 5 and 9")


#------------------------------ Short hand if else statements


a=330000
b=3303
a1=33
b1=225
print("A") if a>b else print("=") if a==b else print("B")
print("a1 greater") if a1>b1 else print("b1 greater")

c=9 if a>b else 0
print(c)


#------------------------------ Enumerate Function

marks=[12,56,87,95,9,56,72,1]
#index=0
#for mark in marks:

#for index, mark in enumerate(marks):
for index, mark in enumerate(marks,start=1):
    print(mark)
    if(index==3):
        print("Awesome marks")
    #index +=1




#------------------------------ import

import pandas
pandas.read_csv()


import math
result1 =math.floor(4.3213459)
result2 =math.sqrt(9)
print(result1)
print(result2)


from math import sqrt as s,pi
#from math import sqrt,pi
#from math import *
result3 =s(9)*pi
print(result3)


import math as m
result4=m.sqrt(9)*m.pi 
print(result4)


import math
print(dir(math))
print(math.nan,type(math.nan))




from main2 import welcome, main2
import math

welcome()
print(main2)


'''

print("github check")































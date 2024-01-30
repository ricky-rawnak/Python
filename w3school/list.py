
#--------------------- List

'''
--uses third [] bracket
--List items are ordered, changeable, and allow duplicate values.

'''
'''
list1=["apple","banana","cherry"]
list2=["kiwi","apple","cherry","banana","kiwi","cherry"]
list3=[2,5,3,9,1,4]
list4=[True,False,False]
list5=["abc",41,True,29,"male"]
list6=list(("apple","banana","cherry"))

print(list1,"\n")
print(list2,"\n")
print(len(list1),"\n")
print(list3,"\n")
print(list4,"\n")
print(list5,"\n")
print(type(list1),"\n")
print(list6,"\n")
'''


#--------------------- List methods

'''
#append-> join
m1=["dragonfruit","lichie"]
m1.append("strawberry")
print((m1),"\n")

m2=["john","sia","aden","emily"]
m3=["usa","france","germam"]
m2.append(m3)
print((m2),"\n")

#clear
m4=["asia","africa","europe"]
m4.clear()
print((m4),"\n")

#copy
m5=["red","blue","red","green"]
x=m5.copy()
print(x,"\n")

#count
x1=m5.count("red")
print(x1,"\n")

points=[1,41,5,9,7,14,5,4,3,5,9,12,5,76]
x2=points.count(5)
print(x2,"\n")


points1=(7,9,5,2)
m6=["a","b","c"]
m6.extend(points1)

#index
m7=["bmw","ford","volvo","prada"]
x3=m7.index('prada')
print(x3,"\n")

x4=points.index(9)
print(x4,"\n")

#extend
m8 = ['apple', 'banana', 'cherry']
m9 = ['Ford', 'BMW', 'Volvo']
m8.extend(m9)
print(m8,"\n")

#insert
m10=["soup","wonton","chips"]
m10.insert(1,"drinks")
print(m10,"\n")

#pop-> removes the specified element
m11=['watch','laptop','mobile','tv']
# m11.pop(1) 
# print(m11) #['watch','mobile','tv']

x5=m11.pop(1)
print(x5,"\n")

#remove
m12=["dell","lenovo","acer","hp"]
m12.remove("dell")
print(m12,"\n")

#reverse
m13=["lion","cat","tiger","dog","zebra"]
m13.reverse()
print(m13,"\n")

#sort
m14=["cloud","sky","river","air"]
#->ascending
m14.sort()
print(m14)

#->descending
m15=["cloud","sky","river","air"]
m15.sort(reverse=True)
print(m15)
'''

'''
#->by length

#len
def myFunc(e):
    return len(e)
cars=['Ford', 'Mitsubishi', 'BMW', 'VW']
cars.sort(key=myFunc)
print(cars,"\n")


def myFunc1(e):
    return e['year']
cars1=[
    {'car':'Ford','year':'2021'},
    {'car':'Mitsubishi','year':'2000'},
    {'car':'BMW','year':'2019'},
    {'car':'Prada','year':'2001'}
]
cars1.sort(key=myFunc1)
print(cars1,"\n")


def myFunc2(e):
    return len(e)
cars2=['Ford', 'Mitsubishi', 'BMW', 'VW']
cars2.sort(reverse=True,key=myFunc2)
print(cars2,"\n")

'''


#--------------------- Access Items
'''
thislist=["apple","banana","cherry", "orange", "kiwi", "melon", "mango"]


print(thislist[1])
print(thislist[-1])
print(thislist[2:5])    #cherry orange kiwi
print(thislist[:4])     #"apple","banana","cherry", "orange"
print(thislist[2:])     #"cherry", "orange", "kiwi", "melon", "mango"
print(thislist[-4:-1])  #7-4:7-1 =>3:6 "orange", "kiwi", "melon"

if "apple" in thislist:
    print("Yes,'apple' is in fruits list")

'''


#--------------------- Change Item Value

'''
thislist1=["apple","banana","cherry", "orange", "kiwi", "melon", "mango"]

thislist1[1]="strawberry"
print(thislist1,"\n")


thislist2=["apple","banana","cherry", "orange", "kiwi", "melon", "mango"]
thislist2[1:3]=["avacado","strawberry"]
print(thislist2,"\n")


thislist3=["apple","banana","cherry"]
thislist3[1:2]=["avacado","strawberry"]
print(thislist3,"\n")


thislist4=["apple","banana","cherry"]
thislist4[1:3]=["strawberry"]
print(thislist4,"\n")


thislist5=["apple","banana","cherry", "orange", "kiwi", "melon", "mango"]
thislist5.insert(2,"jackfruit")
print(thislist5,"\n")


'''

#--------------------- Add List Items
'''
#add an item to the end of the list
thislist6=["apple","banana","cherry"]
thislist6.append("strawberry")
print(thislist6,"\n")


thislist7=["apple","banana","cherry"]
tropical=["mango", "pineapple", "papaya"]
thislist7.extend(tropical)
print(thislist7)


thislist8=["apple","banana","cherry"]
thistuple=("kiwi","orange")
thislist8.extend(thistuple)
print(thislist8)

'''

#--------------------- Remove List Items

'''

thislist9=["cherry","apple","banana","cherry"]
thislist9.remove("cherry")
print(thislist9)


thislist10=["apple","banana","cherry"]
thislist10.pop(0)
print(thislist10)


thislist11=["apple","banana","cherry"]
thislist11.pop()
print(thislist11)   #If you do not specify the index, the pop() method removes the last item


thislist12=["apple","banana","cherry"]
#del thislist12[2]
del thislist12
#print(thislist12)


thislist13=["apple","banana","cherry"]
thislist13.clear()
print(thislist13) 

'''



#--------------------- Loop Lists

'''
thislist14=["apple","banana","cherry"]
for x in thislist14:
    print(x,"\n")
for i in range(len(thislist14)):
    print(thislist14[i],"\n")


thislist15=["apple","banana","cherry"]
j=0
while j<len(thislist15):
    print(thislist15[j])
    j=j+1

thislist16=["apple","banana","cherry"]
[print(x1) for x1 in thislist16]

'''

#--------------------- List Comprehension


fruits =["apple","banana","cherry","kiwi","mango"]
newlist=[]
for x in fruits:
    if "a" in x:
        newlist.append(x)
print(newlist,"\n")


fruits1 =["apple","banana","cherry","kiwi","mango"]
newlist1=[]
for y in fruits1:
    if "e" in y:
        newlist1.append(y)
print(newlist1,"\n")


fruits2 =["apple","banana","cherry","kiwi","mango"]
#newlist2=[x1 for x1 in fruits2 if "a" in x1]
#newlist2=[x1 for x1 in fruits2 if x1!="apple"]
newlist2=[x1 for x1 in fruits2]
print(newlist2,"\n")


newlist3=[x2 for x2 in range(10)]
print(newlist3,"\n")


newlist4=[x3 for x3 in range(10) if x3<5]
print(newlist4,"\n")


newlist5=[x.upper() for x in fruits]
print(newlist5,"\n")


newlist6=['hello' for x in fruits]
print(newlist6,"\n")


newlist7=[x if x!="banana" else "orange" for x in fruits]
print(newlist7,"\n")




















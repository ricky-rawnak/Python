
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




























































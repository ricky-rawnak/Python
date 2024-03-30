
#1
x=14
y=3.1416298938498492481123458266482
z=22/7
m=1.
n=True

print(x)
print(type(x))
print(y)
print(type(y))
print(z)
print(type(z))
print(m)
print(type(m))
print(n)
print(type(n))

#2
rounded_pi=round(z,3)
print(rounded_pi)
print(type(rounded_pi))

#3
k=(1<2)
print(k)
print(type(k))

l=(21<5)
print(l)
print(type(l))

k=not l
print(k)
print(type(k))

#4
s="Hello! Programmers!"
print(s)
print(type(s))
print(len(s))

s1=""
print(s1)
print(type(s1))
print(len(s1))

s2="1.342"
print(s2)
print(type(s2))
print(len(s2))

s3=float(s2)
print(s3)
print(type(s3))

s4="abc"+"def"
print(s4)
print(type(s4))
print(len(s4))

s5="abc"*3
print(s5)
print(type(s5))
print(len(s5))



#------------------------ Exercise

#1
# Define a float
y1 = 1.
print(y1)
print(type(y1))

# Convert float to integer with the int function
z1 = int(y1)
print(z1)
print(type(z1))

#2
print(int(1.2321))
print(int(1.747))
print(int(-3.94535))
print(int(-2.19774))

#3
print(3*True)
print(-3.1*True)
print(type("abc"*False))
print(len("abc"*False))


#4
def get_expected_cost(beds, baths, has_basement):
    value = 80000+30000*beds+10000*baths+40000*has_basement
    return value
costs_hotel=get_expected_cost(1,1,False)
print(costs_hotel)

#5
print(False + False)
print(True + False)
print(False + True)
print(True + True)
print(False + True + True + True)

#6
def cost_of_project(engraving, solid_gold):
    cost = solid_gold*(100+10*len(engraving))+(not solid_gold)*(50+7*len(engraving))
    return cost

#7
project_one = cost_of_project("Charlie+Denver", True)
print(project_one)

project_two = cost_of_project("08/10/2000", False)
print(project_two)
















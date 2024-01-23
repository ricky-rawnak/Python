
#--------------------- Arithmetic Operators

# (+     -   *   /   %   **  //)

'''
p=10
q=3

print(p+q)
print(p-q)
print(p*q)
print(p/q)
print(p%q)
print(p**q) # 10*10*10
print(p//q,"\n") # rounds the result down to the nearest whole number
'''

#--------------------- Assignment Operators

#(=  +=  -=  *=  /=  %=  //=     **=     &=  |=  ^=  >>=  <<=)
'''
Decimal   Binary
-------   ------
   0      0000
   1      0001
   2      0010
   3      0011
   4      0100
   5      0101
   6      0110
   7      0111
   8      1000
   9      1001
  10      1010
  11      1011
  12      1100
  13      1101
  14      1110
  15      1111


Bitwise AND (&) Truth Table:
    0 & 0 = 0
    0 & 1 = 0
    1 & 0 = 0
    1 & 1 = 1
  
Bitwise OR(|) Truth Table:
    0 | 0 = 0
    0 | 1 = 1
    1 | 0 = 1
    1 | 1 = 1

Bitwise XOR(^) Truth Table:
    0 ^ 0 = 0
    0 ^ 1 = 1
    1 ^ 0 = 1
    1 ^ 1 = 0      
'''


'''
q1=q2=q3=q4=q5=q6=q7=q8=q9=q10=q11=q12= 5


q1 += 3
print(q1)

q2 -= 3
print(q2)

q3 *= 3
print(q3)

q4 /= 3
print(q4)

q5 %= 3
print(q5)

q6 //= 3
print(q6)

q7 **= 3
print(q7)

q8 &= 3
print(q8)

q9 |= 3
print(q9) # 111=7

q10 ^= 3
print(q10) # 110=6

q11 >>= 3
print(q11)

q12 <<= 3
print(q12)

'''

#--------------------- Comparison  Operators

'''
q1=5
p1=3

#Equal
print(q1==p1,"\n")

#Not equal
print(q1!=p1,"\n")

#Greater than
print(q1>p1,"\n")

#Less than
print(q1<p1,"\n")

#Greater than equal
print(q1>=p1,"\n")

#Less than equal
print(q1<=p1,"\n")

'''

#--------------------- Identity  Operators


r=["apple","kiwi"]
s=["apple","kiwi"]
t=r
'''
print(r is t) #same value
print(r is s) #Not same object
print(r == s,"\n") #same value


#--------------------- Membership  Operators

print("kiwi" in r)
print("mango" not in r)

'''

#--------------------- Bitwise Operators

'''
#AND            
110 (6)
011 (3)
---
010 (2)


#OR
110
011
---
111 (7)


#XOR
110
011
---
101 (5)


#NOT
011
---
100 (-4)


#ZERO FILL "LEFT" SHIFT(<<)
0011(3) -> insert 2 zero's in right
----
1100(12)


#ERO FILL "RIGHT" SHIFT(>>)
1000(8)
----
0010(2)

'''

print(6 & 3) #2
print(6 | 3) #7
print(6 ^ 3) #5
print(~3)    #-4
print(3<<2)  #12
print(8>>2,"\n")  #2


#--------------------- Operator Precedence

#Parentheses
print((6+3)-(6+3)) # 9-9=0
print((20+5)-(20-5)) # 25-15=10
print(100+5*3) #100+15=115
print(100-5*3) #100-15=85
print(5+4-7+3,"\n") #((5+4)-7)+3=2+3=5

#Exponentiation
print(100-3*3*3) #100-27= 73

#Unary(plus,minus,not)
print(100 + ~3) #100+ -4=>100-4=> 96

#Bitwise left and right shifts
print(8>>4-2) #8>>2=>1000(8)=>0010(2)=>2

#BITWISE And
print(6 & 2+1) #6&3=> 110(6),(011)3=>010(2)=>2

#BITWISE OR
print(6 | 2+1) #6|3=>111(7)=>7

#BITWISE XOR
print(6 ^ 2+1) #6^3=>101(5)=>5

#comparison
print(5==4+1) #True

#Logical NOT
print(not 5==5) #false
print(not 5==3) #true

#Logical AND
# In Python, 0, False, None, and empty sequences (like an empty string or list) are considered false. All other values are considered true.
print(1 or 2 and 3) #1 or true = 1 or 3=1

#Logical OR
print(4 or 5 +10 or 8) #4 or 15 or 8=4









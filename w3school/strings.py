
#--------------------- Strings

# Basic Strings
'''
s="silver"
s1="""
This is a multiline string,
Twinkle twinkle little star
How I wonder what you are!!!
"""
s2="Aden, Laura, Kiana, Ethane, Jake"

print("hi")
print('hi')
print(s)
print(s1)
print(f"{s2} strings character position :",s2[6],s2[1],s2[9])


#Looping
for s3 in 'dolphin':
    print(s3)

#length,check,if-not
s4="A journey by bus"
print(len(s4))

print("by" in s4)   #or
if "journey" in s4:
    print("Yes, 'journey is present")

print("car" not in s4)  #or
if "car" not in s4:
    print("No")

'''

#--------------------- Slicing Strings
# (star:end)
# (star:end:step)

# Positive value indicates counting from the left
# Negative value indicates counting from the right
# How many indices to skip between

'''

for negative 
=string(:-x)
=len(string)-x
[small:big]

'''

'''
#positive
Index:   0  1  2  3  4  5  6  7  8  9 10 11 12
Letter:  H  e  l  l  o  ,     W  o  r  l  d  !

starting index is inclusive,
ending index is exclusive

#negative
Index:  -13 -12 -11 -10 -9 -8 -7 -6 -5 -4 -3 -2 -1
Letter:   H   e   l   l  o  ,     W  o  r  l  d  !
'''

'''
#positive indexing
s5="Hello, World!"
print(s5[2:5]) # llo
print(s5[:5]) # Hello
print(s5[2:]) # llo, World!
print(s5[5:9]) # , Wo
print(s5[2]) # l
print(s5[1:8]) # ello, W

#negative indexing
print(s5[-5:-2]) #  orl
print(s5[-9:-7]) #  o,
print(s5[2:-7]) #  llo,
print(s5[-3:11]) #  l

#step index
print(s5[2:12:1]) # llo, World
print(s5[::2]) # Hlo ol!
print(s5[2:12:5]) # lW
print(s5[1:10:2]) # [1:10]=>ello, Wor(skips 2)=>el,Wr
'''
'''

s6="right ya! bro"
print(len(s6)) #13
print(s6[:])

print(s6[2:]) #  ght ya! bro
print(s6[:7]) #  right y
print(s6[4:9]) # t ya!

print(s6[-12:-7]) # 13-12=13-7 =>1:6
                 #  ight 
print(s6[0:-2]) # 0:13-2=>0:11
               #  right ya! b 
print(s6[-9:-4]) # 4:9 => t ya!
print(s6[10:-2]) #10:11 => b
#print(s6[-4:8]) # 9:8 =>error

s7="Carry"
print(s7[-4:-2]) #  1:3 # ar

'''

#--------------------- Modify Strings

'''
strip() method removes any whitespace
split() method splits the string into substrings
'''
'''

s8="DomestiC, animaL"
s9="    DomestiC animaL "

print(s8.upper())
print(s8.lower())
print(s8.replace("Dom","Hir"))
print(s8.split(","))

print(f"The string '{s9}' after removing whitespace:",s9.strip(),"\n")

'''

#--------------------- Concatenation

'''
s10="Green"
s11="Grass"

sc=s10+s11
sc1=s10+" "+s11

print(sc)
print(sc1)

'''
#--------------------- Format

#s12="3044"
#we cannot combine strings and numbers
#sc2="Quantity of Green grass is: "+sc12
#print(sc2)

'''

s13=5
s14=297
s15=51.22

sc2="Quantity of Green grass is: {}"
print(sc2.format(s12))

sc3="I want to order {} burgers, my item no is {} for {} dollars"
sc4="I want to pay {2} dollars for {0} burgers , my item no is {1}"

print(sc3.format(s13,s14,s15))
print(sc4.format(s13,s14,s15))

'''

#--------------------- Escape Character

'''
# Error -> s16="So called "Vikings" from the west"
s16="So called \"Vikings\" from the west"
s17='It\'s ok'
s18="Insert \\ one backlash"
s19="This represents\nNew line!\n"
s20="This represents\rCarriage return!"
s21="This\tcreates tab"
s22="This\bcreates backspace(erases one char)"


print(s16)
print(s17)
print(s18)
print(s19)
print(s20)
print(s21)
print(s22)

'''

#--------------------- Methods

s23="skY is blue!"
s24="The {dish} is {taste}"
s25="pay9234"
s26="4565"
s27="ricky"
s28="H\te\tl\tl\to\t!\n "
s29="He loves apple which is raw,but she does not like apple"
s30=" "
s31="My Dog Tom"
s32="NOW"

'''
print("This Converts the first character to upper case:",s23.capitalize(),"\n")
print("Converts string into lower case:",s23.casefold(),"\n")
print("Returns a centered string:",s23.center(30,"*"),"\n") #adds padding
print("Returns an encoded version of the string:",s23.encode(),"\n")
print("Returns true if the string ends with the specified value:",s23.endswith("!"),"\n")
print("Sets the tab size of the string:",s23.expandtabs(4),"\n")
print("Searches the string for a specified value:",s23.find("is"),"\n")
print("Formats specified values in a string: The {}".format(s23),"\n")
print("Returns the position of where it was found:",s23.index("l"),"\n")

print("Formats specified values in a string: ",s24.format_map({'dish':'egg','taste':'delicious'}),"\n")

print("Returns True if all characters in the string are alphanumeric:",s25.isalnum(),"\n")
print("True if all characters in the string are ascii characters:",s25.isascii(),"\n")

print("Returns True if all characters in the string are in the alphabet:",s26.isalpha(),"\n")
print("True if all characters in the string are decimals(0-9):",s26.isdecimal(),"\n")
print("True if all characters in the string are digits:",s26.isdigit(),"\n")


print(s23.isprintable())
print(s29.count("apple"))
print(s25.isnumeric())
print(s26.isnumeric())
print(s27.islower())
print("True if it has alphanumeric letters (a-z) and (0-9), or underscores (_):",s27.isdigit(),"\n")
print(s30.isspace())
print(s31.istitle())
print(s32.isupper())


'''
'''
s33=("John","Alex","Kevin")
print("...".join(s33))

s34={"color":"black","box":"square"}
print("CHECK".join(s34))

print(s27.ljust(20),"a name")

s35=" food  "
print(s35.lstrip())
print((",,,,,.....cool").lstrip(",.c"))

s36="Rocks on"
result=s36.maketrans("R","S")
print(s36.translate(result))

s37="Hi Sam"
result1=s37.maketrans("maS","aiL")
print(s37.translate(result1))


print(s29.partition("which"))
print(s29.replace("apple","mango"))
print("Favorite",s35.rstrip())
print(s37.split())

s38="Thank you\nCome again"
print(s38.splitlines())


print(s23.swapcase())

s39="hello b2b2b2 and 3g3g3g london"
print(s39.title())

s40="40h"
print(s40.zfill(10))

'''

#--------------------- String Formatting

price=33
txt="The price is {} dollars"
txt1="The price is {:.2f} dollars"

print(txt.format(price))
print(txt1.format(price))

myorder="I have a {color}, it is {shape} in look"
print(myorder.format(color="Red",shape="star"))





















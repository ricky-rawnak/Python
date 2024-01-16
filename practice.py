'''
##------------------------------ printing numbers from 1 to 5
print("1 2 3 4 5")

##------------------------------ Print with Variables

#Declare a variable name and assign your name to it. Then print a message using that variable, like "Hello, [name]!".
name="Ricky"
print("Hello, "+name+"!")
print(f"Hello, {name}!")

#Create two variables num1 and num2 with numerical values and print their sum.
num1=7
num2=2
sum=num1+num2
print(sum)
'''
##------------------------------ Multi-line Print

#Print a poem or any multi-line text of your choice.
# print('''Twinkle Twinkle
# Little start!
# How I wonder, What Your are!''')
'''
#Use the sep and end parameters to print three words separated by commas, and the line should end with "End of line.
print("Cat", "Dog", "Lion",sep=",",end=" End with line.")

##------------------------------ User Input and Conditional Statements

#Use the input function to ask the user for their age and print a message based on whether they are a minor (under 18) or an adult.
age=int(input("\nEnter age: "))
if(age>18):
    print("Adult")
else:
    print("Minor")

#Create a program that asks the user to input two numbers, then prints whether the first number is greater than, equal to, or less than the second number.
a1=int(input("Enter first number: "))
a2=int(input("Enter second number: "))
if(a1>a2):
    print("First number is greater than the second number")
elif(a1==a2):
    print("Equal numbers")
else:
    print("First number is less than the second number")

##------------------------------ List Manipulation

#Create a list of your favorite fruits and print each fruit on a new line.
fruitList=["mango","orange","banana","kiwi","papaya"]
for fruit in fruitList:
    print(fruit)

#Add a new fruit to the list and print the updated list.
fruitList.append("Jackfruit") #append adds in list
print(fruitList)

'''




















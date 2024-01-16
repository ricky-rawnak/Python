'''
##------------------------------ Simple Calculator

a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Addition of",a,"+",b,"=",a+b)
print("Substraction of",a,"-",b,"=",a-b)
print("Multiplication of",a,"*",b,"=",a*b)
print("Division of",a,"/",b,"=",a/b)


##------------------------------ Temperature Converter

celsius=float(input("Enter temperature in celsius: "))
fehrenheit=((9/5)*celsius)+32
print(f"Fehrenheit: ",fehrenheit)


##------------------------------ String Manipulation

user_name=input("Enter full name: ")
print(user_name)
print(user_name.upper())
print(user_name.lower())
print(user_name.title())


##------------------------------ Age Calculator

current_year=int(input("Enter current year: "))
birth_year=int(input("Enter the year you are born: "))
age=current_year-birth_year
print("Your age: ",age)


##------------------------------ BMI Calculator

height=float(input("Enter your height(meter): "))
weight=float(input("Enter your wight(kilograms): "))
BMI=weight/(height*height)
print(f"The BMI is:",BMI)

'''
##------------------------------ Number Guessing Game

# guess_num=int(input("Guess a number between(1-100): "))
# if(guess_num<1 or guess_num>100):
#     print("Enter correct number")   
# else:
#     print(f"The number is:",guess_num)

#solution=>
import random
random_n=random.randint(1,100)
guesses_taken=0
while True:
    guess=int(input("Guess a number between(1-100): "))
    guesses_taken +=1
    if(guess==random_n):
        print("Correct guess! The number is",random_n)
        print("Number of  guesses",guesses_taken)
        break
    elif(guess<random_n):
        print("Too low! try again")
    else:
        print("Too high! try again")   

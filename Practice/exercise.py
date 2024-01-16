'''
#------------------------------ Calculator

a=int(input("Enter a: "))
b=int(input("Enter b: "))
print("Addition of",a,"+",b,"=",a+b)
print("Substraction of",a,"-",b,"=",a-b)
print("Multiplication of",a,"*",b,"=",a*b)
print("Division of",a,"/",b,"=",a/b)
print("Floor divider of",a,"//",b,"=",a//b)
print("Modular of",a,"%",b,"=",a%b)

#------------------------------ Time

import time
t=time.strftime('%H:%M:%S')
#print("Current time: ",t)
hour=int(time.strftime('%H'))
hour=int(input("Enter the hour: "))
print(hour)

if(0<=hour<12):
    print("Good morning")
elif(12<=hour<15):
    print("Good afternoon")
elif(15<=hour<18):
    print("Good noon")
elif(18<=hour<20):
    print("Good evening")
else:
    print("Goodnight")


#------------------------------ KBC with list

#List called questions that contains a series of sublists
#The last element of each sublist is the correct answer option.
questions=[
    ["What is the capital of France?","Berlin", "London", "Paris", "Rome",3],
    ["Who wrote 'Romeo and Juliet'?","Charles Dickens","William Shakespeare","Jane Austen","Mark Twain",2],
    ["What is the chemical symbol for gold?","Ag","Au","Fe","Hg",2],
    ["In which year did the Titanic sink?","1912","1920","1901","1931",1],
    ["Which planet is known as the 'Red Planet'?","Venus","Jupiter","Saturn","Mars",4],
    ["What is the largest ocean on Earth?"," Atlantic Ocean","Indian Ocean","Pacific Ocean","Southern Ocean",3],
    ["What is the largest mammal in the world??","Elephant","Giraffe","Blue whale","Gorilla",3],
    ["What is the largest desert in the world?", "Sahara Desert", "Gobi Desert", "Arabian Desert", "Antarctic Desert", 1],
    ["What is the capital of Japan?", "Beijing", "Tokyo", "Seoul", "Bangkok", 2],
    ["Which scientist developed the theory of relativity?", "Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla", 2],
]

#prize amount associated with each question
levels=[1000,2000,3000,5000,10000,20000,40000,80000,160000,320000]

#to keep track of the total prize
money=0
for i in range(0,len(questions)):
    question=questions[i]

    print(f"\n\nQuestions for $.{levels[i]}\n")
    print(question[0])
    print(f"a. {question[1]}       b. {question[2]}")
    print(f"c. {question[3]}       d. {question[4]}")
    reply=int(input("Enter your answer (1-4) or 0 to quit: "))
    if(reply==0):
        money=levels[i-1]
        break
    if(reply==question[-1]):
        print(f"Correct answer, you have won $ {levels[i]}")
        if(i==4):
            money=10000
        elif(i==9):
            money=320000
        elif(i==14):
            money=10000000
    else:
        print("Wrong answer")
        break
print(f"You can take home $ {money}")

'''

#------------------------------ secret code

# st="I am useless"
# coding=True
# if(coding):
#     pass
# else:
#     pass



# import random
# def encode(msg):
#     words=msg.split()
#     encoded_words=[]
#     for word in words:
#         if(len(word)>=3):
        

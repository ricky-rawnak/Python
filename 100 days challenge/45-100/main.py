
'''
#------------------------------ if __name__ == "__main__"

import user
#name.greetings()


#------------------------------ OS Model

import os
if(not os.path.exists("data")):
    os.mkdir("data")
for i in range(0,10):
    #os.mkdir(f"data/Day{i+1}")
    os.rename(f"data/Day{i+1}", f"data/Tutorial{i+1}")


import os
folders=os.listdir("data")
#print(folders)
for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))


import os
folders=os.listdir("data")
print(os.getcwd())


#------------------------------ Local vs Global Variables

x=4
print(x)
def hello():
    x=5
    print(f"The local x is {x}")
    print("Hello Coders")

print(f"The global x is {x}")
hello()
x=5
print(f"The global x is {x}")


'''

x1=10       #global
def my_func():
    global x1
    x1=4
    y=5     #local
    print(y)
my_func()
print(x1)
#print(y) # will throw error as y is local variable





















































#1
print(2>3)

#2
var1=1
var2=3
print(var1<1)
print(var2>=var1)

#3
def evaluate_temp(temp):
    msg="Normal temperature"
    if(temp>38):
        msg="Fever!"
    return msg
print(evaluate_temp(37))      
print(evaluate_temp(39))      


#4
def evaluate_temp(temp):
    if(temp>38):
        msg="Fever!"
    else:
        msg="Normal temperature!"
    return msg
print(evaluate_temp(37))      
print(evaluate_temp(39)) 

#5
def evaluate_temp(temp):
    if(temp>38):
        msg="Fever!"
    elif temp>35:
        msg="Normal temperature!"
    else:
        msg="Low temperature!"
    return msg
print(evaluate_temp(36))      
print(evaluate_temp(32)) 

#6
def get_tax(earnings):
    if(earnings<12000):
        tax_owned=0.25*earnings
    else:
        tax_owned=0.30*earnings
    return tax_owned
ana_tax=print(get_tax(9000))
bob_tax=print(get_tax(15000))

#7
def get_dose(weight):
    # Dosage is 1.25 ml for anyone under 5.2 kg
    if weight < 5.2:
        dose = 1.25
    elif weight < 7.9:
        dose = 2.5
    elif weight < 10.4:
        dose = 3.75
    elif weight < 15.9:
        dose = 5
    elif weight < 21.2:
        dose = 7.5
    # Dosage is 10 ml for anyone 21.2 kg or over
    else:
        dose = 10
    return dose
print(get_dose(12))



#-------------------- exercise


#1
def get_grade(score):
    if score>=90:
        grade="A"
    elif score>=80:
        grade="B"
    elif score>=70:
        grade="C"
    elif score>=60:
        grade="D"
    else:
        grade="F"
    return grade
print(get_grade(85))
print(get_grade(49))


#2
def cost_of_project(engraving,solid_gold):
    if solid_gold==True:
        cost=100+10*len(engraving)
    else:
        cost=50+7*len(engraving)
    return cost
print(cost_of_project("cool",1))


#3
def get_water_bill(num_gallons):
    if num_gallons<=8000:
        bill= 5*num_gallons/1000
    elif num_gallons<=22000:
        bill=6*num_gallons/1000
    elif num_gallons<=30000:
        bill=7*num_gallons/1000
    else:
        bill=10*num_gallons/1000
    return bill
print(get_water_bill(8000))
























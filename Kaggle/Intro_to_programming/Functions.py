
#1

#header
def add_three(input_var):
#body
    output_var=input_var+3
    return output_var

new_number=add_three(10)
print(new_number)

#2
def get_pay(num_hours):
    pay_pretax=num_hours*15
    pay_aftertax=pay_pretax*(1-0.12)
    return pay_aftertax
# payment=get_pay(40)
payment=get_pay(32)
print(payment)


#3
def get_pay_with_more_inputs(n_hours,hourly_wage,tax_bracket):
    pretax_pay=n_hours*hourly_wage
    aftertax_pay=pretax_pay*(1-tax_bracket)
    return aftertax_pay
higer_pay_aftertax=get_pay_with_more_inputs(40,24,0.22)
print(higer_pay_aftertax)

same_pay_fulltime=get_pay_with_more_inputs(40,15,0.12)
print(same_pay_fulltime)


#4
def print_msg():
    print("Hello, Siri!")
    print("Good morning!")
print_msg()


#-------------- exercise

#1
def get_expected_cost(beds,baths):
    value=80000+30000*beds+10000*baths
    return value

#2
option_one=get_expected_cost(2,3)
option_two=get_expected_cost(3,2)
option_three=get_expected_cost(3,3)
option_four=get_expected_cost(3,4)

print(option_one)
print(option_two)
print(option_three)
print(option_four)


#3
def get_cost(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sq=sqft_walls+sqft_ceiling
    gallons_needed=total_sq/sqft_per_gallon
    cost=cost_per_gallon*gallons_needed
    return cost
project_cost = get_cost(432,144,400,15)
print(project_cost)

#4
import math
test_value=2.17
rounded_value=math.ceil(test_value)
print(rounded_value)

#5
def get_actual_costs(sqft_walls, sqft_ceiling, sqft_per_gallon, cost_per_gallon):
    total_sq=sqft_walls+sqft_ceiling
    gallons_needed=total_sq/sqft_per_gallon
    gallons_to_buy=math.ceil(gallons_needed)
    cost=cost_per_gallon*gallons_to_buy
    return cost
costs_to_buy=get_actual_costs(432, 144, 400, 15)
costs_to_buy2= get_actual_costs(594, 288, 400, 15)
print(costs_to_buy)
print(costs_to_buy2)


























#1
flowers="pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(type(flowers),"\n")
print(flowers,"\n")


#2
flowers_list=["pink primrose","hard-leaved pocket orchid","canterbury bells","sweet pea","english marigold","tiger lily","moon orchid","bird of paradise","monkshood","globe thistle"]
print(type(flowers_list),"\n")
print(flowers_list,"\n")


#3
print(len(flowers_list),"\n")


#4
print("First entry:",flowers_list[0])
print("Second entry:",flowers_list[1])
print("Last entry:",flowers_list[9],"\n")

#5
print("First 3 entries",flowers_list[:3])
print("Final 2 entries",flowers_list[-2:],"\n")

#6
flowers_list.remove("tiger lily")
print(flowers_list,"\n")

#7
flowers_list.append("snapdragon")
print(flowers_list,"\n")


#8
sales=[139, 128, 172, 139, 191, 168, 170]

print(len(sales))
print(type(sales))
print(sales[:4])
print("Entry at index 2",sales[2],"\n")
print("Maximum",max(sales),"\n")
print("Minimum",min(sales),"\n")
print("Total sales",sum(sales),"\n")
print("Sales on first five days",sum(sales[:5])/5)

#--------------- exercise

#1
menu = ['stewed meat with onions', 'bean soup', 'risotto with trout and shrimp',
       'fish soup with cream and onion', 'gyro']

menu.remove('bean soup')
menu.append('roasted beet salad')
print(menu)

#2
num_customers = [137, 147, 135, 128, 170, 174, 165, 146, 126, 159,141, 148, 132, 147, 168, 153, 170, 161, 148, 152,141, 151, 131, 149, 164, 163, 143, 143, 166, 171]

print(len(num_customers))
print(sum(num_customers[:7])/7)
print(sum(num_customers[-7:])/7)
print(max(num_customers))
print(min(num_customers))


#3
flowers = "pink primrose,hard-leaved pocket orchid,canterbury bells,sweet pea,english marigold,tiger lily,moon orchid,bird of paradise,monkshood,globe thistle"

print(flowers.split(","))


#4
alphabet = "A.B.C.D.E.F.G.H.I.J.K.L.M.N.O.P.Q.R.S.T.U.V.W.X.Y.Z"
address = "Mr. H. Potter,The cupboard under the Stairs,4 Privet Drive,Little Whinging,Surrey"

print(alphabet.split("."))
print(address.split(","))

#5
test_ratings=[1,2,3,4,5]
test_liked=[i>=4 for i in test_ratings]
print(test_liked)

#6
def percentage_liked(ratings):
    list_liked = [i >= 4 for i in ratings]
    percentage_liked = sum(list_liked)/len(list_liked)
    return percentage_liked

print(percentage_liked([1, 2, 3, 4, 5, 4, 5, 1]))


#7
def percentage_growth(num_users,yrs_ago):
    growth = (num_users[len(num_users)-1] - num_users[len(num_users)-yrs_ago-1])/num_users[len(num_users)-yrs_ago-1]
    return growth

num_users_test = [920344, 1043553, 1204334, 1458996, 1503323, 1593432, 1623463, 1843064, 1930992, 2001078]
print(percentage_growth(num_users_test, 1))
print(percentage_growth(num_users_test, 7))







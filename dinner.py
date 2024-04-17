#Developed by: Hamza Khamissa
#Date: Started January 31
#Date: Completed Febuary 7
#Desc: A program that serves guests in a simulation of a resturant 
#Inputs: Number of guests, dietary restrictions, tip amounts
#Outputs: Food given, total price owed (before and after tax, and after tip), listed out food  

#Lets start off with pricing the items
#These are constants, we identified them as
PIZZA_COST = 44.50
PASTA_COST = 48.99
FALAFEL_COST = 52.99
STEAK_COST = 49.60
BEVERAGE_COST = 5.99

#Lets define the separator between the code, i like to use them to keep the code clean
def seperator():
    print("--------------------")

#Asking for the amount of guests we have 
guests=int(input("Please enter the number of invitees:"))
    
#These counters are used to track the amount of times each item has been ordered
#These variables will be critical for listing out the bill showing the amount of people
pizzaCount = 0
pizzaTotal = 0

pastaCount = 0
pastaTotal = 0

falafelCount = 0
falafelTotal = 0

steakCount = 0
steakTotal = 0

beverageCount = 0
beverageTotal = 0

#Now asking each guest their order preferences 
#Created a counter to loop the amount of times we must ask dietary restricitons, i < guests where guests is our input value
#keto != "y" allows us to only accept "y" as a yes
totalCost = 0
i = 0
while i < guests:
    print("Please enter the order details for invitee Number %d/%d" % (i + 1, guests ))
    keto = input("Do you want a keto friendly meal?")
    if keto != "y":
        keto = "n"
    vegan = input("Do you want a vegan meal?")
    if vegan != "y":
        vegan = "n"
    gluten = input("Do you want a Gluten-free meal?")
    if gluten != "y":
        gluten = "n"
    seperator()

    #here we are listing out what allows for each item to be selected, ex "y", "y", "y", gives you falafel!
    #Then the count for falafel goes up by 1
    #And the price for falafel is added to the total, the rest of the items work the same
    if keto == 'y' and vegan == 'y' and gluten == 'y':
        falafelTotal += FALAFEL_COST
        falafelCount += 1
        totalCost += FALAFEL_COST

    elif keto == 'y' and vegan == 'y' and gluten == 'n':
        pizzaTotal += PIZZA_COST
        pizzaCount += 1
        totalCost += PIZZA_COST
    
    elif keto == 'y' and vegan == 'n' and gluten == 'y':
        steakTotal += STEAK_COST
        steakCount += 1
        totalCost += STEAK_COST

    
    elif keto == 'n' and vegan == 'y' and gluten == 'n':
        pastaTotal += PASTA_COST
        pastaCount += 1
        totalCost += PASTA_COST

    else: 
        beverageTotal += BEVERAGE_COST
        beverageCount += 1
        totalCost += BEVERAGE_COST
        #The else statement allows the option if dietary restirctions cannot be matched 
 
    i+= 1 #This is to ensure the loop does not continue forever

#adding this output will list how many guests ordered what and giving the subtotal for the pruchase

#Asking for the tip for the server
tip =  int(input("How much do you want to tip your server (% percent)?"))

#Listing out the bill
print("You have %d invitees with the following orders:" % (guests))
print("%d invitees ordered Pizza. The cost is: $%.02f" % (pizzaCount, round(pizzaTotal,2)))
print("%d invitees ordered Pasta. The cost is: $%.02f" % (pastaCount, round(pastaTotal, 2)))
print("%d invitees ordered Falafel. The cost is: $%.02f" % (falafelCount, round(falafelTotal, 2)))
print("%d invitees ordered Steak. The cost is: $%.02f" % (steakCount, round(steakTotal, 2)))
print("%d invitees ordered Beverge. The cost is: $%.02f" % (beverageCount, round(beverageTotal, 2)))

#Calculating total after tax, using subtotal of items, multiplied by 1.13
#All items are roudned to the second decimal point.
print("The total cost before tax is $%0.2f" % (round(totalCost, 2)))
totalCostWithTax = totalCost * 1.13 
print ("The total cost after tax is $%0.2f" % (round(totalCostWithTax, 2)))

#Calculating tip from total cost after tax with a percentage forumula
#Continuing rounding to the second decimal point
totalCostWithTaxAndTip = totalCostWithTax * (100+tip) / 100
print("The total cost after %d%% tip is $%d" % (tip, round(totalCostWithTaxAndTip)))
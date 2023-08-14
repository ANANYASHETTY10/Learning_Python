#Code for function 
#def name of the function(element used in a function):
#print("-------"+element used in a function)
#name of the function("element used in a function")

print(" Welcome to the Ticket Counter")
def person_1(name):
    name=input(name+":Which movie ticket you want?")
person_1("Cashier")

def person_2(name):
     name=input("I want 2 tickets of "+name)
person_2("Drishyam")

def person_1_2(seats):
    seats = input("Which 2 seats you want to book?= ")
    print("I want 2 "+seats+" seats")
person_1_2("seats") 

def person_1_2(payment,bill):
    payment=input("Would you like to pay money through cash or online transaction?= ")
    print("I want to pay in "+payment)
    price_of_1_ticket=150
    price_of_2_ticket= 2*float(price_of_1_ticket)
    bill=input("Your total bill is of rupees = "+str(+price_of_2_ticket))
person_1_2("payment","bill")

print("*********************************************")
print("Welcome to the food counter")
def person_1(name):
    print(name+":How can I help you?")
person_1("Distributor")

def person_1_2(food,juice,dessert):
    food=input("What you want to have? =")
    juice=input("Which juice you would like to have? =")
    dessert=input("What you will eat as a dessert? =")
    print("I would like to have some "+food+" alongwith "+juice+" and "+dessert+" in my meal")
person_1_2("food","juice","desert")

def person_1_2(payment,bill,food,juice,dessert):
    payment=input("Would you like to pay money through cash or online transaction?= ")
    print("I want to pay in"+payment)
    price_of_food=150
    price_of_juice=80
    price_of_dessert=120
    print("Total Amt.of "+food+ " is:"+str(price_of_food))
    print("Total Amt.of " +juice+" is:"+str(price_of_juice))
    print("Total Amt.of "+dessert+ " is:"+str(price_of_dessert))
    total_food_bill = price_of_food + price_of_juice + price_of_dessert
    bill=input("Your total bill is of rupees = "+str(total_food_bill)+"rupees")
person_1_2("payment","bill","food","juice","dessert") 
print("Thankyou for visiting")





     


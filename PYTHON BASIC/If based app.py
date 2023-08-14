#this function takes the value of total piece sold and price of per piece and returns the total income
def total_income(piece,price):
    return piece*price

pers_1=input("What is your company name? :")
product1_mostseller=input("Which is the most selling product in your company? =")            
price_per_product1=int(input("What is the price of one "+product1_mostseller))#"int" is used because we want to take input as a integer value "python takes input bydefault in string"
pers1_sale=int(input("How much pieces sold in this month? :"))#"int" is used because we want to take input as a integer value "python takes input bydefault in string"
#"Person1_income" stores the value which is return by total_income function
Person1_income = total_income(pers1_sale, price_per_product1)#We give the value of total sale and price per product

pers_2=input("What is your company name? :")
product2_mostseller=input("Which is the most selling product in your company? =")            
price_per_product2=int(input("What is the price of one "+product2_mostseller))#"int" is used because we want to take input as a integer value "python takes input bydefault in string"
pers2_sale=int(input("How much pieces sold in this month? :"))#"int" is used because we want to take input as a integer value "python takes input bydefault in string"
#"Person2_income" stores the value which is return by total_income function
Person2_income = total_income(pers2_sale, price_per_product2)#We give the value of total sale and price per product

if float(Person2_income)>float(Person1_income):
    print(pers_2+" Company is in profit")
elif  float(Person1_income)>float(Person2_income):
    print( pers_1+"Company is in profit")
else:
    print(pers_1+" and "+pers_2+" both the companies have same sales")

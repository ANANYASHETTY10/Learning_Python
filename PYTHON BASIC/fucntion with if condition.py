def totalvalue(product,price):
    return product*price

pers1_name=input("What is your name?: ")
pers1_product=input("Which product you bought?: ")
pro1_price=int(input("What is the price of "+pers1_product))
pro1_quantity=int(input("Qty:"))
pro_price=totalvalue(pro1_price,pro1_quantity)
bill_pers1=print(pers1_name+" your Total bill is "+str(pro_price))

pers2_name=input(" What is your name?:  ")
pers2_product=input("Which product you bought?: ")
pro2_price=int(input("What is the price of "+pers2_product))
pro2_quantity=int(input("Qty:"))
pro_total_price=totalvalue(pro2_price,pro2_quantity)
bill_pers2=(print(pers2_name+" your Total bill is "+str(pro_total_price)))

if float(pro_total_price)>(pro_price):
   print(pers2_name+"has more to pay than "+pers1_name)
elif float(pro_price)>(pro_total_price):
    print(pers1_name+"has more to pay than "+pers2_name)
else:
    print(pers1_name+" and "+pers2_name+" have same amount to pay")


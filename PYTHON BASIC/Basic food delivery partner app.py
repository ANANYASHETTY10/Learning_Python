"""welcome=input("Welcome to Zomato Supermarket\n")"""
print("Welcome to Zomato Supermarket")
product_name_1=input("What is your first product? =")
product_price_1=input("What is the price of(1 piece of)1st product? =")
Quantity_price_1=input("What is the quantity of 1st product? = ")
product_name_2=input("What is your second product? =")
product_price_2=input("What is the price of(1 piece of)2nd product? =")
Quantity_price_2=input("What is the quantity of 2nd product? = ")
product_name_3=input("What is your third product? =")
product_price_3=input("What is the price of(1 piece of)3rd product? =")
Quantity_price_3=input("What is the quantity of 3rd product? = ")

result_price_product1=float(product_price_1)*float(Quantity_price_1)
result_price_product2=float(product_price_2)*float(Quantity_price_2)
result_price_product3=float(product_price_3)*float(Quantity_price_3)

print("**************")

print("The price of " +product_name_1+ " is "+str(result_price_product1))
print("The price of " +product_name_2+ " is "+str(+result_price_product2))
print("The price of " +product_name_3+ " is "+str(+result_price_product3))

print("***************")

result_all_products=result_price_product1 + result_price_product2 + result_price_product3
print("Your total bill is of Rs."+str(result_all_products))

#Finding 1% value of actual amount
percent_1=result_all_products/100
#Finding 6% value for CGST
CGST=percent_1*6

print("CGST 6.00% "+str(CGST))
print("SGST 6.00% "+str(CGST))
print("Payable Amt.= "+str(result_all_products+CGST+CGST))
print("Thankyou for visiting\nHave a nice day ")



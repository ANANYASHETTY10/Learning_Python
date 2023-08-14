from math import*
print("Meena Kapda Bhandaar")
name_1=input("What is your name? =")
name_2=input("What is your name? =")
name_3=input("What is your name? =")
 
Total_piece_of_cloth=100
Total_price_of_cloth=input("How much is the total cost for 100 metre of clothes? =")
price_of_1metre_cloth= float(Total_price_of_cloth) /float(Total_piece_of_cloth)
print("How is the cost of 1metre of cloth? ="+str(price_of_1metre_cloth))
piece_taken_by_each_person_1=input("How much piece of cloth you have taken by "+name_1+" (in metres)? =")
piece_taken_by_each_person_2=input("How much piece of cloth you have taken by "+name_2+" (in metres)? =")
piece_taken_by_each_person_3=input("How much piece of cloth you have taken by "+name_3+" (in metres)? =")

price_person1= float(price_of_1metre_cloth)*float(piece_taken_by_each_person_1)
price_person2= float(price_of_1metre_cloth)*float(piece_taken_by_each_person_2)
price_person3= float(price_of_1metre_cloth)*float(piece_taken_by_each_person_3)

bill_of_person_1=input("Total Amt. of "+name_1+" is : "+str(price_person1))
bill_of_person_2=input("Total Amt. of "+name_2+ "is : "+str(price_person2))
bill_of_person_3=input("Total Amt. of "+name_3+" is : "+str(price_person3))

Total_piece_of_cloth_by_all=float(piece_taken_by_each_person_1) + float(piece_taken_by_each_person_2) + float(piece_taken_by_each_person_3)
print("Total piece product they bought altogether ="+str(Total_piece_of_cloth_by_all))

remaining_piece_of_cloth = Total_piece_of_cloth - Total_piece_of_cloth_by_all
print("Remaining piece of cloth="+str(remaining_piece_of_cloth))

print("Thankyou for shopping")
print("**************")










def fillform():
    filling= input("Do you want to fill admission form:")
    if filling != "yes":
        return print("Something went wrong")
    else: 
       print("Great! Answer the next question")

    Quest_new =input("Which field you want to select? ")
    
    Quest_1=input("Is your 10th grades is above 65%?:")
    if Quest_1 !="yes":
       return print("Please answer the given question!")
    else:
      print("Next question")

    Quest_2=input("Which college you want to select? ")
    Quest_3=input("Phone Number:")
    Quest_4=input("Enter the address:")
    Quest_5=input("Enter your E-mail id:")
    Quest_5=print("Enter you subject marks")
    marks_subject=input("Science:")
    input("Mathematics:")
    input("Social Studies:")
    input("Marathi:")
    input("English:")
    Quest_6=print("Thankyou for responding!")  

fillform()

      


    
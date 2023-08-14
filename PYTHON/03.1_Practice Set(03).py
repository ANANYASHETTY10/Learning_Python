# Write a python program to display a user centred name followed by Good Afternoon using input() function
name=input("Enter you name=\n")
print("Good Afternoon,"+name)

# Write a python program to fill in a letter template given below
letter= '''Dear <|Name|>
Greetings from XYZ company.We are happy to announce that you are selected!
Hoping for a great day ahead!
DATE:<|Date|>'''
name=input("Enter your Name\n")
date=input("Enter the date\n")
letter=letter.replace("<|Name|>",name)
letter=letter.replace("<|Date|>",date)
print(letter)

# Write a python program to find double spaces in the string
string="This is a sentence with double  space"
doublespace= string.find("  ")
print(doublespace)

# Replace the double space from abive problem into single space
string="This is a sentence with double  space  and    fullstop"
string=string.replace("  "," ")
print(string)

# Write a python program to format the following letter using escape sequence character
letter=''' Dear Ananya,Thankyou for your valuable response.We will get back to you shortly.Thankyou!'''
formatted_letter=''' Dear Ananya,\n\tThankyou for your valuable response!\nWe will get back to you shortly.\nRegards KCCEMSR.'''
print(formatted_letter)
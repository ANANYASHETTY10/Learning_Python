"""#If statement part-1

I_like_python=False
I_like_java=False

if I_like_python:
   print('Its my favourite language')
else: print('Python is not your favourite language')

#If 'and' is used then if any of the one variable is false then it's false and "if" condition will not work
if I_like_python and I_like_java:
   print('My favourite language')
else: print('Sorry the following language is not appropriate to use')

#If 'or' is used then if any of the one variable is true then it's true and "if" condition will work
if I_like_python or I_like_java:
   print('My favourite language')
else: print('Sorry the following language is not appropriate to use')

#"elif" is used for else if condition in python.It basically act as a second condition if the first condition is false
if I_like_java:
   print('My use to language is java')
elif I_like_python:
     print('My use to language is python')
else: print('I like either languages')

#if not is used for reversing the boolean value of the given variable 
if not I_like_java:
    print("Its my favourite language")
 
#if statement part-2 

var1= 25
var2= 25
# Here double "equals to" is been taken to check that whether both the variable are same or not if they are not same then the further
# condition will work
if var1==var2:
  print ('yes')
else: 
   print ('no')

#Here "!=" depicts to "not equal" 
if var1!=var2:
   print ('yes')
else: 
   print ('no')

#Here ">" depicts to "greater than"
if var1>var2:
   print ('yes')
else: 
   print ('no')

#Here ">=" depicts to "greater than equal to"
if var1>=var2:
   print ('yes')
else: 
   print ('no')"""

#SMALL APP 

var1="Black"
var2="Red"
var3="Purple" 
var4="Pink"

if var1!=var2:
   print("Your favourite colour is "+var1)
else:
   print("Sorry something went wrong")
print("Thankyou")

 
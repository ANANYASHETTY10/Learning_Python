# If and elif statement --> This is a multiway decision taken by our program due to certain conditions in our code
a=15
# # this is collectively called aa a "if-elif-else ladder"
if(a<2):
    print("The value of a is lesser than 2")
elif(a>10):
    print("The value of a is greater than 10")    
else:
    print("The value of a is not greater than 5 or 10")  
# It will always satisfy only one condition despite of if's or elif's

# # Multiple if statement 
a=12
if(a<6):
    print("The value of a is lesser than 6")
if(a>10):
    print("The value of a is greater than 10")
# if-else condition(if true then print "if statement" if false then print "else statement")
if(a==11):
    print("The value of a is equal to 11")
else:
    print("The value of a is not matched to above condition")

# Program to print yes when the age entered by the user is greater than or equal to 18
a=int(input("Enter your age: "))
if(a>=18):
    print("Yes")
else:
    print("Invalid age")

# Relational Operators(==,>=,<=)
a=12
b=13
if (a<=b):
    print("The value of a & b satisfy the given condition")
else:
    print("The value of a & b remains unsatisfied")
if(a==b):
    print("The value of a is equal to b")
else:
    print("The value of a & b differ from each other")

# Logical operators(and,or,not)
a=int(input("Enter your roll no: "))
if(a>10 and a<=20): #For "AND" both the both operands must be true else false
    print("You are in Group1")
else:
    print("You are in another Group")

if(a>21 or a<=30):#For "OR" any one operand must be true else false
    print("You are in Group2")
else:
    print("You are in other group")

# elif clause is nothing but the same code written from line 4 to 9 of the code

# "is" and "in "
a= None  
if(a is None):
    print("Yes")
else:
    print("No")

a=[32,3,10]
print(30  in a)
 
